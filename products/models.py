from django.db import models

# 🟤 موديل المنتج
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="اسم المنتج"
    )
    description = models.TextField(
        verbose_name="الوصف"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="السعر"
    )
    image = models.ImageField(
        upload_to='products/',  # هذا المجلد يظهر داخل Cloudinary
        verbose_name="صورة المنتج",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"


# 🟤 موديل طلب الجملة
class BulkOrder(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="اسم التاجر أو الشركة"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="رقم الجوال"
    )
    email = models.EmailField(
        verbose_name="البريد الإلكتروني"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="الكمية المطلوبة (كجم)"
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name="ملاحظات إضافية"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الطلب"
    )

    def __str__(self):
        return f"{self.full_name} - {self.quantity} كجم"

    class Meta:
        verbose_name = "طلب جملة"
        verbose_name_plural = "طلبات الجملة"
