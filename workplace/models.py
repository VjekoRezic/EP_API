from django.db import models

class Workplace(models.Model):
    """
    Model representing a workplace.

    This model defines the attributes of a workplace, including its name, code,
    points, and whether it's deleted or not.

    Attributes:
        name (str): The name of the workplace.
        code (str): The code associated with the workplace.
        points (decimal): The points associated with the workplace.
        is_deleted (bool): A flag indicating whether the workplace is deleted or not.

    Methods:
        __str__: Returns the string representation of the workplace.
    """

    name = models.CharField(verbose_name="workplace name", max_length=150)
    code = models.CharField(verbose_name="workplace code", max_length=5)
    points = models.DecimalField(verbose_name="workplace points", decimal_places=2, max_digits=6, default=0)
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)

    def __str__(self) -> str:
        """
        Return a string representation of the workplace.

        Returns:
            str: The name of the workplace.
        """
        return self.name
