from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm

# صفحة تسجيل مستخدم جديد
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "تم إنشاء الحساب بنجاح 🎉")
            return redirect('login')
        else:
            messages.error(request, "حدث خطأ في البيانات. يرجى التحقق من الحقول ❌")
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

# صفحة تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"مرحباً {user.username} 👋 تم تسجيل الدخول بنجاح ✅")
            return redirect('home')  # ← تأكد أن لديك مسار باسم home
        else:
            messages.error(request, "فشل في تسجيل الدخول ❌ تحقق من البيانات")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
