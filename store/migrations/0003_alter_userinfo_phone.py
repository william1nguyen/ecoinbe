# Generated by Django 4.2.5 on 2024-08-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_brand_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
