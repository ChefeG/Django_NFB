# Generated by Django 4.1.3 on 2022-12-05 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_announcements_modelannouncements_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelstatistics',
            old_name='nft_in_sake',
            new_name='nft_in_stake',
        ),
    ]
