# Generated by Django 4.1.7 on 2023-08-19 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_alter_t_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='remember_shortcut',
            fields=[
                ('remember_shortcut_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('f_os', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.os')),
                ('f_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.t_user')),
                ('shortcuts', models.ManyToManyField(to='API.shortcut')),
            ],
            options={
                'verbose_name': 'ショートカット情報',
                'verbose_name_plural': 'ショートカット情報',
            },
        ),
    ]
