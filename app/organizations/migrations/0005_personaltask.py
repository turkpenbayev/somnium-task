# Generated by Django 4.1.2 on 2022-10-22 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_alter_department_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('notify_at', models.DateTimeField()),
                ('notified', models.BooleanField(default=False)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='organizations.personal')),
            ],
        ),
    ]
