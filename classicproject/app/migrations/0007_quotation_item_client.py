# Generated by Django 4.1.3 on 2022-11-24 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_subsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quotation')),
                ('subsection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.subsection')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('quotation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quotation')),
            ],
        ),
    ]
