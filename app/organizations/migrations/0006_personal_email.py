# Generated by Django 4.1.2 on 2022-10-22 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_personaltask'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='email',
            field=models.EmailField(default='ex.turkpenbaev_1997@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
