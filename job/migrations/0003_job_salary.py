# Generated by Django 3.0.3 on 2020-02-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20200218_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]
