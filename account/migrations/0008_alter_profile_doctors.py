# Generated by Django 4.0.3 on 2022-03-13 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_doctor_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctors',
            field=models.ManyToManyField(blank=True, null=True, related_name='customers', to='account.doctor'),
        ),
    ]
