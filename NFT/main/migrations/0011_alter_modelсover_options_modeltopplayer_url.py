# Generated by Django 4.1.3 on 2022-12-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_modelсover_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelсover',
            options={'verbose_name': 'Cover', 'verbose_name_plural': 'Covers'},
        ),
        migrations.AddField(
            model_name='modeltopplayer',
            name='url',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
