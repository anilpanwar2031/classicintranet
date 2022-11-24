# Generated by Django 4.1.3 on 2022-11-24 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_quotation_quot_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quotation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quotation')),
            ],
        ),
    ]
