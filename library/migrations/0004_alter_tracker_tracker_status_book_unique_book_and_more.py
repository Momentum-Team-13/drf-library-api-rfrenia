# Generated by Django 4.0.6 on 2022-07-22 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_tracker_tracker_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='tracker_status',
            field=models.CharField(choices=[('Want to Read', 'Want to Read'), ('Currently Reading', 'Currently Reading'), ('Read/Done', 'Read/Done')], default='Want to Read', max_length=20),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_book'),
        ),
        migrations.AddConstraint(
            model_name='tracker',
            constraint=models.UniqueConstraint(fields=('book', 'user'), name='unique_tracker'),
        ),
    ]