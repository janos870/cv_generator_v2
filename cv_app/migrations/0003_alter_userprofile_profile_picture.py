# Generated by Django 5.0.1 on 2024-02-02 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0002_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='profile_pictures/'),
        ),
    ]
