from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="المستخدم"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )
    quantity = models.PositiveIntegerField(verbose_name="الكمية")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")

    def __str__(self):
        return f"طلب #{self.id} - {self.product.name} بواسطة {self.user.username}"

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"
