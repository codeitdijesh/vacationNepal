# Generated by Django 4.1.4 on 2023-01-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_package_it'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='itenary',
        ),
        migrations.AddField(
            model_name='package',
            name='isUnderRated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='package',
            name='it',
            field=models.JSONField(default='{}'),
        ),
    ]
