# Generated by Django 5.0.2 on 2024-02-22 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intervention', '0007_alter_appointment_appointmentdate_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='report',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='report',
            name='student',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
