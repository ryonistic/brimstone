from django.test import TestCase
import datetime
# from django.conf import settings
from .models import Admission
from courses.models import Course


class AdmissionTests(TestCase):
    def setUp(self):
        test_course = Course.objects.create(name='Sample Course', description='A sample course here', stream='1')
        test_course.save()
        test_application = Admission.objects.create(
        student_name = 'John Doe', 
        date_of_birth = datetime.date(1999, 5, 5),
        father_name = 'Jack Doe', 
        mother_name = 'Mary Doe', 
        qualification_level = '2', 
        email = 'doe@ramalama.com', 
        phone = '9999999899', 
        gender = 'M', 
        address = '123, Holy Shtreet', 
        state = '1', 
        course = test_course)
        test_application.save()

    def test_admission_was_requested(self):
        application = Admission.objects.get(student_name='John Doe')
        print(application)
        student = f'{application.student_name}'
        date_of_birth = f'{application.date_of_birth}'
        father_name = f'{application.father_name}'
        mother_name = f'{application.mother_name}'
        qualification_level = f'{application.qualification_level}'
        email = f'{application.email}'
        phone = f'{application.phone}'
        gender = f'{application.gender}'
        address = f'{application.address}'
        state = f'{application.state}'
        self.assertEqual(student, 'John Doe')
        self.assertEqual(date_of_birth, '1999-05-05')
        self.assertEqual(father_name, 'Jack Doe')
        self.assertEqual(mother_name, 'Mary Doe')
        self.assertEqual(qualification_level, '2')
        self.assertEqual(email, 'doe@ramalama.com')
        self.assertEqual(phone, '9999999899')
        self.assertEqual(gender, 'M')
        self.assertEqual(address, '123, Holy Shtreet')
        self.assertEqual(state, '1')
