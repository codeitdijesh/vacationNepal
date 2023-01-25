# Generated by Django 4.1.4 on 2023-01-05 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0008_alter_packages_itenary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='featured_img',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('packageName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.packages')),
            ],
        ),
    ]
