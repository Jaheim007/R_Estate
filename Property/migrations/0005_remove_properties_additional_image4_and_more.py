# Generated by Django 4.1.2 on 2022-10-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0004_remove_properties_more_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properties',
            name='additional_image4',
        ),
        migrations.RemoveField(
            model_name='properties',
            name='additional_image5',
        ),
        migrations.AlterField(
            model_name='properties',
            name='main_image',
            field=models.ImageField(upload_to='Property_images'),
        ),
    ]
