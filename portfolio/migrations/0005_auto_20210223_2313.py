# Generated by Django 3.1.1 on 2021-02-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_certificates_procat_projects_skillset_sociallink'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='tittle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
