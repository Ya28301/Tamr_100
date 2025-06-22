from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import home_view  # ← استيراد العرض للصفحة الرئيسية

urlpatterns = [
    # الصفحة الرئيسية
    path('', home_view, name='home'),

    # لوحة تحكم الأدمن
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('accounts/', include('accounts.urls')),  # تسجيل الدخول / تسجيل الخروج / التسجيل
    path('products/', include('products.urls')),  # المنتجات + الطلب بالجملة + تواصل معنا
    path('orders/', include('orders.urls')),      # الطلبات
]

# دعم ملفات الميديا من Cloudinary أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
