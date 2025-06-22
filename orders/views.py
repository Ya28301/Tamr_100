# orders/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

# عرض الطلبات الخاصة بالمستخدم
@login_required
def order_page(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order.html', {'orders': orders})
