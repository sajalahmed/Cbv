# Generated by Django 3.2.9 on 2021-11-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.TextField(null=True),
        ),
    ]
