from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput,
        min_length=8,
        help_text="كلمة المرور يجب أن تحتوي على 8 أحرف على الأقل."
    )
    confirm_password = forms.CharField(
        label="تأكيد كلمة المرور",
        widget=forms.PasswordInput
    )
    phone = forms.CharField(
        label="رقم الجوال",
        max_length=15
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # نحذف confirm_password من الحفظ لأنه ليس حقلًا في النموذج

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("البريد الإلكتروني مستخدم بالفعل.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("كلمتا المرور غير متطابقتين.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])  # تشفير كلمة المرور
        if commit:
            user.save()
        return user
