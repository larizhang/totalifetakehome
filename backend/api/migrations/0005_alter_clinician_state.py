# Generated by Django 5.1.7 on 2025-03-19 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_appointment_id_alter_clinician_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinician',
            name='state',
            field=models.CharField(max_length=30),
        ),
    ]
