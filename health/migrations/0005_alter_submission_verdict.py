# Generated by Django 4.0.3 on 2022-03-13 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_usersymptom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='verdict',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
