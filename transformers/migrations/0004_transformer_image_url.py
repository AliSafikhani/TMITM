# Generated by Django 5.0.6 on 2024-06-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformers', '0003_remove_transformer_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='transformer',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
