"""This model will only be altered by the 
admissions.views's document approving function. 
All fields are to borrowed from the Document model and
Admission model as those two instances will be combined after
verification of documents and that combination will be a student instance."""
import uuid
from django.db import models
from courses.models import Course
from users.models import CIEmailField


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = CIEmailField(unique=True, max_length=150)
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField()
    father_name = models.CharField(blank=True, max_length=150)
    mother_name = models.CharField(blank=True, max_length=150)
    gender = models.CharField(max_length=150)
    address = models.CharField(max_length=400)
    state = models.CharField(max_length=200)
    student_photo = models.ImageField()
    highschool_diploma = models.FileField()
    address_proof = models.FileField()
    undertaking = models.FileField()
    def __str__(self):
        return str(self.name)
