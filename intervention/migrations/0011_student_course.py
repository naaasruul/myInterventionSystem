# Generated by Django 5.0.2 on 2024-02-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intervention', '0010_alter_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
