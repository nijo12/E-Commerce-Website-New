# Generated by Django 4.0.2 on 2023-02-21 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0002_categorydb'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=500, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Profile')),
            ],
        ),
    ]
