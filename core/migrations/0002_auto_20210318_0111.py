# Generated by Django 3.1.7 on 2021-03-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='slug',
        ),
        migrations.AddField(
            model_name='host',
            name='type_org',
            field=models.CharField(default='School', max_length=100),
        ),
    ]
