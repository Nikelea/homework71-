# Generated by Django 4.0.3 on 2022-03-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscribs',
            field=models.ManyToManyField(related_name='subscrib', to='accounts.profile'),
        ),
    ]
