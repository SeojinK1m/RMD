# Generated by Django 3.1.7 on 2021-04-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_eatery_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='eatery',
            name='url',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
