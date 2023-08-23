from django.db import models
from workcenter.models import WorkCenter
from django.conf import settings

class WO_Category(models.Model):
    """
    Model representing a category for work orders.

    Attributes:
        name (CharField): The name of the category.
        is_deleted (BooleanField): Indicates whether the category is deleted.

    Methods:
        __str__: Returns the string representation of the category.
    """

    name = models.CharField(max_length=150, verbose_name="Category name")
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)

    def __str__(self) -> str:
        """
        Return the string representation of the category.

        Returns:
            str: The name of the category.
        """
        return self.name
    

class WO_Status(models.Model):
    """
    Model representing a status for work orders.

    Attributes:
        name (CharField): The name of the status.
        is_deleted (BooleanField): Indicates whether the status is deleted.

    Methods:
        __str__: Returns the string representation of the status.
    """

    name = models.CharField(max_length=150, verbose_name="name")
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)

    def __str__(self) -> str:
        """
        Return the string representation of the status.

        Returns:
            str: The name of the status.
        """
        return self.name
    

class WorkOrder(models.Model):
    """
    Model representing a work order.

    Attributes:
        title (CharField): The title of the work order.
        description (TextField): A description of the work order.
        start_time (DateTimeField): The start time of the work order (auto-generated on creation).
        due_time (DateTimeField): The due time of the work order.
        complete_time (DateTimeField): The completion time of the work order.
        work_center (ForeignKey): The work center associated with the work order.
        category (ForeignKey): The category of the work order.
        created_by (ForeignKey): The user who created the work order.
        assigned_to (ForeignKey): The user to whom the work order is assigned.
        status (ForeignKey): The status of the work order.
        created_at (DateTimeField): The creation time of the work order (auto-generated).
        updated_at (DateTimeField): The last update time of the work order.
        is_deleted (BooleanField): Indicates whether the work order is deleted.

    Methods:
        __str__: Returns the string representation of the work order.
        get_status_display: Returns the display name of the status.
        created_by_get_full_name: Returns the full name of the user who created the work order.
        assigned_to_get_full_name: Returns the full name of the user to whom the work order is assigned.
    """

    title = models.CharField(max_length=150, verbose_name="title")
    description = models.TextField(verbose_name="description")
    start_time = models.DateTimeField(verbose_name="start", auto_now_add=True, null=True)
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
        """
        Return the string representation of the work order.

        Returns:
            str: The title of the work order.
        """
        return self.title
    
    def get_status_display(self):
        """
        Return the display name of the status.

        Returns:
            str: The display name of the status.
        """
        return self.status.name
    
    def created_by_get_full_name(self):
        """
        Return the full name of the user who created the work order.

        Returns:
            str: The full name of the user who created the work order.
        """
        return self.created_by.__str__()
    
    def assigned_to_get_full_name(self):
        """
        Return the full name of the user to whom the work order is assigned.

        Returns:
            str: The full name of the user to whom the work order is assigned.
        """
        return self.assigned_to.__str__()
