# Generated by Django 5.1.1 on 2024-09-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('umidity', models.CharField(max_length=20)),
                ('sunlight', models.CharField(max_length=20)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('categories', models.ManyToManyField(blank=True, to='api.category')),
            ],
        ),
    ]
