# Generated by Django 4.2.1 on 2023-06-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visiteCandidats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidats',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]