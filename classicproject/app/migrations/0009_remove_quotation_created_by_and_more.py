# Generated by Django 4.1.3 on 2022-11-24 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_quotation_created_by_quotation_creation_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='quotation',
            name='creation_on',
        ),
    ]
