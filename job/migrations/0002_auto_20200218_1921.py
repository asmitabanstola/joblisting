# Generated by Django 3.0.3 on 2020-02-18 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='company',
            new_name='company_name',
        ),
    ]
