# Generated by Django 5.0 on 2023-12-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Fname',
            field=models.CharField(max_length=100, verbose_name='FNAME'),
        ),
    ]