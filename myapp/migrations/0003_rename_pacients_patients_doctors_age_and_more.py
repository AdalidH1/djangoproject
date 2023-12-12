# Generated by Django 5.0 on 2023-12-12 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_pacients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pacients',
            new_name='Patients',
        ),
        migrations.AddField(
            model_name='doctors',
            name='age',
            field=models.IntegerField(default=20, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctors',
            name='location',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctors',
            name='phone',
            field=models.IntegerField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]
