# Generated by Django 4.1.1 on 2022-12-12 14:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_rename_project_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='featured_img',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='package',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
