# Generated by Django 4.0.6 on 2023-04-14 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='hidden_desc',
            new_name='dimensions',
        ),
    ]
