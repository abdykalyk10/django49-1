from django.db import models
from django.contrib.auth.models import User
from datetime import date


class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15, default='+996', blank=True)
    address = models.TextField()
    work_years = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    department = models.CharField(max_length=100)
    education = models.CharField(max_length=255)
    skills = models.TextField()
    hired_date = models.DateField(default=date.today)

    def save(self, *args, **kwargs):
        if self.work_years <= 2:
            self.salary = 30000
        elif 3 <= self.work_years <= 5:
            self.salary = 50000
        elif self.work_years >= 6:
            self.salary = 70000
        super().save(*args, **kwargs)
