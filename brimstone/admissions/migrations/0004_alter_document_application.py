# Generated by Django 4.0.4 on 2022-04-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0003_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='application',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
