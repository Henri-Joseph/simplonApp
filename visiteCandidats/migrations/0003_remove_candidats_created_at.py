# Generated by Django 4.2.1 on 2023-06-04 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visiteCandidats', '0002_alter_candidats_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidats',
            name='created_at',
        ),
    ]
