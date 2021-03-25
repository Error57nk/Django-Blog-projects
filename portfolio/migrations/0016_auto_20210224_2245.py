# Generated by Django 3.1.1 on 2021-02-24 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20210224_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='proLink',
            field=models.CharField(blank=True, default='javascript:void(0)', max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('images', models.ImageField(default='hdef.jpg', upload_to='portfolio/hobbies')),
                ('des', models.CharField(blank=True, max_length=200, null=True)),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.bio')),
            ],
        ),
    ]
