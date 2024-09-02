# Generated by Django 5.1 on 2024-09-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='comosition',
            new_name='composition',
        ),
        migrations.AddField(
            model_name='medicine',
            name='med_image',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]
