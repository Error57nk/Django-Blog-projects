# Generated by Django 3.1.1 on 2021-02-24 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20210224_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificates',
            old_name='tittle',
            new_name='title',
        ),
    ]
