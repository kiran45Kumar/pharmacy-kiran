# Generated by Django 5.0.4 on 2024-09-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_rename_update_at_customer_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
