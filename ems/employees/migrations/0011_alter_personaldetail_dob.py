# Generated by Django 5.0.6 on 2024-07-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_alter_personaldetail_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
