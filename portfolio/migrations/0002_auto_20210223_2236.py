# Generated by Django 3.1.1 on 2021-02-23 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='phone1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bio',
            name='phone2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
