# Generated by Django 3.1 on 2020-08-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200808_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='img/default-product-img.jpg', upload_to='img/'),
        ),
    ]
