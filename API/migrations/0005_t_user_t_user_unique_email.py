# Generated by Django 4.1.7 on 2023-08-19 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_rename_key1_shortcut_f_key1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='t_user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ユーザーID')),
                ('email', models.EmailField(max_length=100, verbose_name='メールアドレス')),
                ('password', models.CharField(max_length=50, verbose_name='パスワード')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'ユーザー情報',
                'verbose_name_plural': 'ユーザー情報',
            },
        ),
        migrations.AddConstraint(
            model_name='t_user',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_email'),
        ),
    ]
