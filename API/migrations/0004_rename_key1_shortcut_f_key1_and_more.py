# Generated by Django 4.1.7 on 2023-08-15 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_keymap_key_alter_keymap_placeholder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortcut',
            old_name='key1',
            new_name='f_key1',
        ),
        migrations.RenameField(
            model_name='shortcut',
            old_name='key2',
            new_name='f_key2',
        ),
        migrations.RenameField(
            model_name='shortcut',
            old_name='key3',
            new_name='f_key3',
        ),
    ]