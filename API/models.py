from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class key(models.Model):
    key_id = models.AutoField(primary_key=True)
    key_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key_name

class os(models.Model):
    os_id = models.AutoField(primary_key=True)
    os_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.os_name

class keymap(models.Model):
    keymap_id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=10)
    placeholder = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.key)

class shortcut(models.Model):
    shortcut_id = models.AutoField(primary_key=True)
    shortcut_name = models.CharField(max_length=100)
    f_os = models.ForeignKey(os, on_delete=models.CASCADE)
    f_key1 = models.ForeignKey(keymap, on_delete=models.CASCADE, related_name='key1', null=True, blank=True)
    f_key2 = models.ForeignKey(keymap, on_delete=models.CASCADE, related_name='key2', null=True, blank=True)
    f_key3 = models.ForeignKey(keymap, on_delete=models.CASCADE, related_name='key3', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shortcut_id}:{self.shortcut_name} "
    



class t_user(models.Model):
    user_id = models.AutoField("ユーザーID",primary_key=True)
    email = models.EmailField("メールアドレス",max_length=100)
    password = models.CharField("パスワード",max_length=128)
    created_at = models.DateTimeField("作成日時",auto_now_add=True)
    updated_at = models.DateTimeField("更新日時",auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]
        verbose_name = 'ユーザー情報'
        verbose_name_plural = 'ユーザー情報'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

class remember_shortcut(models.Model):
    remember_shortcut_id = models.AutoField(primary_key=True)
    f_user = models.ForeignKey(t_user, on_delete=models.CASCADE)
    f_os = models.ForeignKey(os, on_delete=models.CASCADE)
    shortcuts = models.ManyToManyField(shortcut)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '間違えたショートカット情報'
        verbose_name_plural = '間違えたショートカット情報'

    def __str__(self):
        return f"{self.f_user.email}:{self.f_os.os_name}"
