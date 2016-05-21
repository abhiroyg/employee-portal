from __future__ import unicode_literals

import datetime
from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    dob = models.DateField(default=datetime.date.today())
    is_admin = models.BooleanField(default=False)
    joining_date = models.DateField(default=datetime.date.today())
    current_address = models.TextField()
    permanent_address = models.TextField()
    pan_number = models.CharField(max_length=10, unique=True)

    class Meta:
        unique_together = ('first_name', 'middle_name', 'last_name')

class File(models.Model):
    """Contains all the files corresponding to an employee.

    These are just paths of files stored in server's filesystem.
    To see to what all employees an admin has to upload stuff,
    we will iterate over the table for that `file_type`.

    We will never show `file_path` in UI. We will show an `uploaded`
    flag. It will be red if `file_path` is empty, else green.

    TODO: Should we have a list of upload dates?
    Should we have a first upload date?
    """
    FORM_16 = 'f16'
    FILE_TYPE_CHOICES = (
        (FORM_16, 'Form16'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=1000, unique=True)
    file_type = models.CharField(max_length=100,
        choices=FILE_TYPE_CHOICES,
        default=FORM_16)
    uploaded_date = models.DateTimeField(auto_now=True)

class DeviceLicense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    devicelicense_type = models.CharField(max_length=100,
        choices=DEVICELICENSE_TYPE_CHOICES,
        default=LAPTOP)
    devicelicense_id = models.CharField(max_length=100, primary_key=True)
