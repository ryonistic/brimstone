# Generated by Django 4.0.4 on 2022-04-23 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0007_alter_document_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='application',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admissions.admission'),
        ),
    ]
