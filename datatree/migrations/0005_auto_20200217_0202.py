# Generated by Django 3.0.3 on 2020-02-17 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datatree', '0004_auto_20200217_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relation',
            name='person',
            field=models.CharField(max_length=50),
        ),
    ]
