# Generated by Django 4.1.2 on 2022-10-22 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_rename_personalpostion_departmentpersonalpostion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_deparments', to='organizations.department'),
        ),
    ]
