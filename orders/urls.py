# orders/urls.py

from django.urls import path
from .views import order_page  # ← استيراد الفيو

urlpatterns = [
    path('', order_page, name='orders-list'),  # ← اسم واضح للرابط
]
