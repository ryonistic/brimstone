# Generated by Django 4.0.4 on 2022-04-22 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_daytime_room_subject_lesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='name',
            new_name='type',
        ),
    ]
