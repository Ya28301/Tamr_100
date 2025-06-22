from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import BulkOrderForm  # نموذج الطلب بالجملة
from django.views.decorators.csrf import csrf_protect  # حماية من هجمات CSRF

# عرض الصفحة الرئيسية
def home_view(request):
    return render(request, 'home.html')

# عرض صفحة الطلب بالجملة
@csrf_protect
def bulk_order_view(request):
    if request.method == 'POST':
        form = BulkOrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ تم إرسال الطلب بنجاح.")
            return redirect('bulk-order')  # تفادي إعادة الإرسال عند التحديث
        else:
            messages.error(request, "❌ تأكد من صحة البيانات المدخلة.")
    else:
        form = BulkOrderForm()

    return render(request, 'products/bulk_order.html', {'form': form})

# عرض قائمة المنتجات
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

# عرض صفحة تواصل معنا
@csrf_protect
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            # يمكن لاحقًا نحفظ البيانات في نموذج أو نرسل بريد
            messages.success(request, "✅ تم إرسال رسالتك بنجاح!")
        else:
            messages.error(request, "❌ جميع الحقول مطلوبة.")
    
    return render(request, 'products/contact.html')
