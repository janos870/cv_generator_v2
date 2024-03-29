# Generated by Django 5.0.1 on 2024-02-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0003_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(default='No education', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.CharField(default='No experience', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='languages',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(upload_to='media/profile_pictures/'),
        ),
    ]
