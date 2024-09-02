# Generated by Django 5.1 on 2024-09-02 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('batches', '0001_initial'),
        ('medicine', '0002_rename_comosition_medicine_composition_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_stock', models.IntegerField()),
                ('reorder_level', models.IntegerField()),
                ('storage_location', models.CharField(max_length=200)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('batch_id', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='batches.batches')),
                ('medicine_id', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
            ],
        ),
    ]