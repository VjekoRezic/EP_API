from django.db import models
from django.conf import settings
from workorder.models import WorkOrder
from workcenter.models import WorkCenter

class Failure(models.Model):
    """
    Represents a reported failure within a work center.

    Attributes:
        name (str): The name of the failure.
        description (str): A detailed description of the failure.
        reported_by (User): The user who reported the failure (Foreign Key to User model).
        created_at (datetime): The timestamp when the failure was created.
        updated_at (datetime): The timestamp when the failure was last updated.
        is_deleted (bool): Indicates if the failure is marked as deleted.
        work_order (WorkOrder): The associated work order (Foreign Key to WorkOrder model).
        work_center (WorkCenter): The work center where the failure occurred (Foreign Key to WorkCenter model).

    Methods:
        __str__: Returns a string representation of the failure.
        get_name: Returns the full name of the user who reported the failure.
    """

    name = models.CharField(
        max_length=150,
        verbose_name="failure name",
        help_text="The name of the failure."
    )
    description = models.TextField(
        verbose_name="failure description",
        help_text="A detailed description of the failure."
    )
    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="reported by",
        related_name="reporter",
        help_text="The user who reported the failure (Foreign Key to User model)."
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True,
        help_text="The timestamp when the failure was created."
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated at",
        null=True,
        help_text="The timestamp when the failure was last updated."
    )
    is_deleted = models.BooleanField(
        verbose_name="is_deleted",
        default=False,
        help_text="Indicates if the failure is marked as deleted."
    )
    work_order = models.ForeignKey(
        WorkOrder,
        on_delete=models.CASCADE,
        verbose_name="work order",
        null=True,
        help_text="The associated work order (Foreign Key to WorkOrder model)."
    )
    work_center = models.ForeignKey(
        WorkCenter,
        on_delete=models.CASCADE,
        verbose_name="work center",
        help_text="The work center where the failure occurred (Foreign Key to WorkCenter model)."
    )

    def __str__(self) -> str:
        """
        Return a string representation of the failure.

        Returns:
            str: The name of the failure.
        """
        return self.name

    def get_name(self):
        """
        Return the full name of the user who reported the failure.

        Returns:
            str: The full name of the user who reported the failure.
        """
        return self.reported_by.get_full_name()
