from django.db import models
from workcenter.models import WorkCenter
from django.conf import settings

class WO_Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Category name")
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)

    def __str__(self) -> str:
        return self.name
    

class WO_Status(models.Model):
    name = models.CharField(max_length=150, verbose_name="name")
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)

    def __str__(self) -> str:
        return self.name
    

class WorkOrder(models.Model):
    title = models.CharField(max_length=150, verbose_name="title")
    description = models.TextField(verbose_name="description")
    start_time = models.DateTimeField(verbose_name="start", null=True)
    due_time = models.DateTimeField(verbose_name="due time", null=True)
    complete_time = models.DateTimeField(verbose_name="complete time", null=True)
    work_center = models.ForeignKey(WorkCenter, on_delete=models.CASCADE, verbose_name="work center")
    category = models.ForeignKey(WO_Category, on_delete=models.CASCADE, verbose_name="order category")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,  verbose_name="creator", related_name="creator")
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,  verbose_name="assignee", related_name="assignee")
    status = models.ForeignKey(WO_Status, on_delete=models.CASCADE, verbose_name="order status")
    created_at = models.DateTimeField(verbose_name="Created at",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", null=True)
    is_deleted = models.BooleanField(verbose_name="is deleted", default=False)

    def __str__(self) -> str:
        return self.title
    