from django.urls import path
from .views import (
    home_view,
    bulk_order_view,
    product_list_view,
    contact_view
)

urlpatterns = [
    path('', home_view, name='home'),                          # الصفحة الرئيسية
    path('bulk-order/', bulk_order_view, name='bulk-order'),   # طلب بالجملة
    path('products/', product_list_view, name='products-list'),# قائمة المنتجات
    path('contact/', contact_view, name='contact'),            # صفحة تواصل معنا
]
