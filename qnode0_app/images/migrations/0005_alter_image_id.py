# Generated by Django 3.2.16 on 2022-12-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
