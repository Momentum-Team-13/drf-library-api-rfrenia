# Generated by Django 4.0.6 on 2022-07-20 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_title_tracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='featured_book',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
