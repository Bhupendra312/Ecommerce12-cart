# Generated by Django 5.0.7 on 2024-07-12 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
