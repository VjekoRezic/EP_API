from django.db import models

from django.db import models
from department.models import Department

class WorkCenter(models.Model):
    name = models.CharField(max_length=150, verbose_name="work center name")
    description = models.TextField(verbose_name="work center description")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="department")
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)

    def __str__(self) -> str:
        return self.name
