from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'order_date']  # عرض الحقول
    search_fields = ['user__username', 'product__name']                 # تمكين البحث
    list_filter = ['order_date']                                        # تصفية حسب التاريخ
