from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from workorder.models import WorkOrder
from workcenter.models import WorkCenter

class Failure(models.Model):
    name = models.CharField(max_length=150, verbose_name="failure name")
    description = models.TextField(verbose_name="failure description")
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="reported by", related_name="reporter")
    created_at = models.DateTimeField(verbose_name="Created at",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", null=True)
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, verbose_name="work order", null=True)
    work_center = models.ForeignKey(WorkCenter, on_delete=models.CASCADE, verbose_name="work center")

    def __str__(self) -> str:
       return self.name
    
    def get_name(self):
        return self.reported_by.get_full_name()
    
    
