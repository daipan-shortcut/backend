# Generated by Django 4.1.7 on 2023-08-19 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_alter_remember_shortcut_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remember_shortcut',
            old_name='Missshortcuts',
            new_name='shortcuts',
        ),
    ]