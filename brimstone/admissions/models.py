from enum import unique
from uuid import uuid4
from django.db import models
from courses.models import Course
from users.models import CIEmailField


class Admission(models.Model):
    LEVEL_CHOICES = (
            ('1', 'Undergraduate'),
            ('2', 'Graduate'),
            ('3', 'Continuing education')
            )
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Others'),
            ('R', 'Rather not say')
            )
    STATE_CHOICES = (
            ('1', 'Andhra Pradesh'),
            ('2', 'Arunachal Pradesh'),
            ('3', 'Assam'),
            ('4', 'Bihar'),
            ('5', 'Chhattisgarh'),
            ('6', 'Goa'),
            ('7', 'Gujarat'),
            ('8', 'Haryana'),
            ('9', 'Himachal Pradesh'),
            ('10', 'Jharkhand'),
            ('11', 'Karnataka'),
            ('12', 'Kerala'),
            ('13', 'Madhya Pradesh'),
            ('14', 'Maharashtra'),
            ('15', 'Manipur'),
            ('16', 'Meghalaya'),
            ('17', 'Mizoram'),
            ('18', 'Nagaland'),
            ('19', 'Odisha'),
            ('20', 'Punjab'),
            ('21', 'Rajasthan'),
            ('22', 'Sikkim'),
            ('23', 'Tamil Nadu'),
            ('24', 'Telangana'),
            ('25', 'Tripura'),
            ('26', 'Uttar Pradesh'),
            ('27', 'Uttarakhand'),
            ('28', 'West Bengal')	
            )

    STATUS_CHOICES = (
            ('0', 'PENDING'),
            ('1', 'COMPLETED')
            )

    student_name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    father_name = models.CharField(blank=True, max_length=150)
    mother_name = models.CharField(blank=True, max_length=150)
    qualification_level = models.CharField(choices=LEVEL_CHOICES, max_length=50)
    email = CIEmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=150)
    address = models.CharField(max_length=400)
    state = models.CharField(choices=STATE_CHOICES, max_length=200)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    admission_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.CharField(choices=STATUS_CHOICES,default='0' ,max_length=15)
    
    def __str__(self):
        return str(self.admission_id)

class Document(models.Model):
    student_photo = models.ImageField()
    highschool_diploma = models.FileField()
    graduate_degree = models.FileField(blank=True, null=True)
    address_proof = models.FileField()
    undertaking = models.FileField()
    verified = models.BooleanField(default=False)
    application = models.OneToOneField(Admission, null=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return str(self.application.admission_id)
