# Generated by Django 4.0.4 on 2022-04-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0009_alter_document_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='graduate_degree',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
