# Generated by Django 4.0.6 on 2022-07-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='tracker_status',
            field=models.CharField(blank=True, choices=[('Want to Read', 'Want to Read'), ('Currently Reading', 'Currently Reading'), ('Read/Done', 'Read/Done')], max_length=20, null=True),
        ),
    ]
