from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from workplace.models import Workplace
from workcenter.models import WorkCenter
from datetime import date

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, father_name, date_of_birth, email, city, password=None, job_title=None, rfid_uid=None, workplace=None, workcenter=None):
        if not email:
            raise ValueError("User must have an email")
        
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.father_name = father_name
        user.date_of_birth = date_of_birth
        user.city = city
        user.job_title = job_title
        user.rfid_uid = rfid_uid
        user.workplace = workplace
        user.workcenter = workcenter
        user.is_deleted = False
        
        user.set_password(password)  # Use Django's method to set hashed password
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, father_name, date_of_birth, email, city, password, job_title=None, rfid_uid=None, workplace=None, workcenter=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            date_of_birth=date_of_birth,
            email=email,
            city=city,
            job_title=job_title,
            rfid_uid=rfid_uid,
            workplace=workplace,
            workcenter=workcenter,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    first_name = models.CharField(verbose_name='First name', max_length=255)
    last_name = models.CharField(verbose_name='Last name', max_length=255)
    father_name = models.CharField(verbose_name="Fathers name", max_length=255)
    date_of_birth = models.DateField(verbose_name='Date of birth')
    email = models.EmailField(verbose_name="email", max_length=150, unique=True)
    city = models.CharField(verbose_name="city", max_length=255)
    job_title = models.CharField(verbose_name="job title", max_length=255, null=True, blank=True)
    rfid_uid = models.CharField(max_length=20, verbose_name='Card ID', unique=True, null=True, blank=True)
    is_deleted = models.BooleanField(verbose_name="is_deleted", default=False)
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE, verbose_name="workplace", null=True, blank=True)
    workcenter = models.ForeignKey(WorkCenter, on_delete=models.CASCADE, verbose_name="work center", null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "father_name", "date_of_birth", "city"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
