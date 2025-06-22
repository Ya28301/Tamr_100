from django.contrib import admin
from .models import Product  # ← تأكد أن هذا هو اسم الموديل المستخدم في models.py

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']  # عرض اسم المنتج والسعر في لوحة التحكم
    search_fields = ['name', 'description']  # تمكين البحث عن طريق الاسم والوصف
