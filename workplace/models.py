from django.db import models

class Workplace(models.Model):
    name = models.CharField(verbose_name="workplace name", max_length=150)
    code = models.CharField(verbose_name="workplace code", max_length=5)
    points = models.DecimalField(verbose_name="workplace points", decimal_places=2, max_digits=6, default=0)
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)

    def __str__(self) -> str:
        return self.name