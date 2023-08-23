from django.db import models
from django.conf import settings

class Department(models.Model):
    """
    Represents a department within the organization.

    Attributes:
        name (str): The name of the department.
        description (str): A detailed description of the department.
        created_at (datetime): The timestamp when the department was created.
        updated_at (datetime): The timestamp when the department was last updated.
        is_deleted (bool): Indicates if the department is marked as deleted.
        manager (User): The manager of the department (Foreign Key to User model).
    """

    name = models.CharField(
        verbose_name="department name",
        max_length=150,
        help_text="The name of the department."
    )
    description = models.TextField(
        verbose_name="description",
        help_text="A detailed description of the department."
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now_add=True,
        help_text="The timestamp when the department was created."
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated at",
        null=True,
        help_text="The timestamp when the department was last updated."
    )
    is_deleted = models.BooleanField(
        verbose_name="is deleted",
        default=False,
        help_text="Indicates if the department is marked as deleted."
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="manager",
        help_text="The manager of the department (Foreign Key to User model)."
    )

    def __str__(self) -> str:
        """
        Return a string representation of the department.

        Returns:
            str: The name of the department.
        """
        return self.name
