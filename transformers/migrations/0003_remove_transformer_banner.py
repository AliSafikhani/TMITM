# Generated by Django 5.0.6 on 2024-06-17 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transformers', '0002_transformer_banner_transformer_operation_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transformer',
            name='banner',
        ),
    ]
