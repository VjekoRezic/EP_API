from django.db import models
from django.conf import settings

class Department(models.Model):
    name = models.CharField(verbose_name="department name", max_length=150)
    description = models.TextField(verbose_name="description")
    created_at = models.DateTimeField(verbose_name="Created at",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", null=True)
    is_deleted = models.BooleanField(verbose_name="is deleted", default=False)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="manager")

    def __str__(self) -> str:
        return self.name
