# Generated by Django 4.1.2 on 2023-04-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='body_shape',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='skin_tone',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
