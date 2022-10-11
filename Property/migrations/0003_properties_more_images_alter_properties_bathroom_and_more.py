# Generated by Django 4.1.2 on 2022-10-11 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0002_alter_properties_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='more_images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='additional_images', to='Property.additionalpropertyimage'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='bathroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties_bathrooms', to='Property.bathrooms'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='bedroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties_bedrooms', to='Property.bedrooms'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='garage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties_garages', to='Property.garages'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='Property_images'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='property_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_property', to='Property.typeproperty'),
        ),
    ]
