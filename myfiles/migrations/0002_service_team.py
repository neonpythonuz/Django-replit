# Generated by Django 4.1.7 on 2023-04-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
                ('malumot', models.TextField()),
                ('rasm1', models.ImageField(upload_to='media')),
                ('rasm2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('rasm3', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=30)),
                ('lavozimi', models.CharField(max_length=40)),
                ('malumot', models.TextField()),
                ('rasm', models.ImageField(upload_to='media')),
            ],
        ),
    ]
