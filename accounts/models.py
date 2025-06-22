from django.db import models

class SampleModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "نموذج"
        verbose_name_plural = "النماذج"
