# Generated by Django 4.1.3 on 2022-11-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_quotation_quot_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='quot_status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]