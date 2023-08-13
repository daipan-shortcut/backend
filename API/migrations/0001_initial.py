# Generated by Django 4.1.7 on 2023-08-13 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='os',
            fields=[
                ('os_id', models.AutoField(primary_key=True, serialize=False)),
                ('os_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='shortcut',
            fields=[
                ('shoortcut_id', models.AutoField(primary_key=True, serialize=False)),
                ('shortcut_name', models.CharField(max_length=100)),
                ('key1', models.CharField(blank=True, max_length=100, null=True)),
                ('key2', models.CharField(blank=True, max_length=100, null=True)),
                ('key3', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('f_os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.os')),
            ],
        ),
    ]
