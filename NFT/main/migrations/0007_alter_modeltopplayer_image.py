# Generated by Django 4.1.3 on 2022-12-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_modeltopplayer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltopplayer',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]