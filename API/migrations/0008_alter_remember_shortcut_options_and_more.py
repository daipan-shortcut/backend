# Generated by Django 4.1.7 on 2023-08-19 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_remember_shortcut'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remember_shortcut',
            options={'verbose_name': '間違えたショートカット情報', 'verbose_name_plural': '間違えたショートカット情報'},
        ),
        migrations.RenameField(
            model_name='remember_shortcut',
            old_name='shortcuts',
            new_name='Missshortcuts',
        ),
    ]
