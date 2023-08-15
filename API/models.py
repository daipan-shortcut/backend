from django.db import models

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
        return f"{self.f_os.os_name}:{self.shortcut_name} "