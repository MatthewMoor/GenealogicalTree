# Generated by Django 3.0.3 on 2020-02-18 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datatree', '0005_auto_20200217_0202'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='people',
            name='f_name',
        ),
        migrations.AddField(
            model_name='people',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datatree.Relation'),
        ),
    ]
