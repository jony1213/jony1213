# Generated by Django 4.0 on 2021-12-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_patient_phone_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]