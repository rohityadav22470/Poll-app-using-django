# Generated by Django 3.2.25 on 2024-08-16 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='test',
            new_name='choice_test',
        ),
    ]
