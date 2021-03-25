# Generated by Django 3.1.1 on 2021-02-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_auto_20210225_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='areaIntrest',
            field=models.TextField(blank=True, default='Electronic', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='bio',
            name='bioabout',
            field=models.TextField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='bio',
            name='biobanner',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bio',
            name='bioindex',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='des',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='procat',
            name='des',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='des',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='projects',
            name='techused',
            field=models.TextField(max_length=100),
        ),
    ]
