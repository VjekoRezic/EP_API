from django.db import models
from department.models import Department

class WorkCenter(models.Model):
    """
    Model representing a work center.

    Attributes:
        name (CharField): The name of the work center.
        description (TextField): A description of the work center.
        department (ForeignKey): The department to which the work center belongs.
        is_deleted (BooleanField): Indicates whether the work center is deleted.

    Methods:
        __str__: Returns the string representation of the work center.
    """

    name = models.CharField(max_length=150, verbose_name="work center name")
    description = models.TextField(verbose_name="work center description")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="department")
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)

    def __str__(self) -> str:
        """
        Return the string representation of the work center.

        Returns:
            str: The name of the work center.
        """
        return self.name
