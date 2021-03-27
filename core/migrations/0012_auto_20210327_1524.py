# Generated by Django 3.1.7 on 2021-03-27 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210327_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='Last_Submission_Date',
        ),
        migrations.AddField(
            model_name='host',
            name='Last_Submission_Date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
