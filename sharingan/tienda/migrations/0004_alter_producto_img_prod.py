# Generated by Django 5.0.6 on 2024-07-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_producto_img_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img_prod',
            field=models.ImageField(null=True, upload_to='../media/tienda'),
        ),
    ]
