# Generated by Django 4.1 on 2024-06-17 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro_api', '0006_rename_name_user_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='titulo',
            new_name='nombre',
        ),
    ]
