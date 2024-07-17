# Generated by Django 5.0.6 on 2024-06-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transformer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('voltage', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
            ],
        ),
    ]
