# Generated by Django 4.0.4 on 2022-04-24 05:25

from django.db import migrations, models
import django.db.models.deletion
import users.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0004_alter_lesson_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('email', users.models.CIEmailField(max_length=150, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField()),
                ('father_name', models.CharField(blank=True, max_length=150)),
                ('mother_name', models.CharField(blank=True, max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=400)),
                ('state', models.CharField(max_length=200)),
                ('student_photo', models.ImageField(upload_to='')),
                ('highschool_diploma', models.FileField(upload_to='')),
                ('graduate_degree', models.FileField(blank=True, null=True, upload_to='')),
                ('address_proof', models.FileField(upload_to='')),
                ('undertaking', models.FileField(upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
