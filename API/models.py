from django.db import models

# Create your models here.
class os(models.Model):
    os_id = models.AutoField(primary_key=True)
    os_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class shortcut(models.Model):
    shoortcut_id = models.AutoField(primary_key=True)
    shortcut_name = models.CharField(max_length=100)
    f_os = models.ForeignKey(os, on_delete=models.CASCADE)
    key1= models.CharField(max_length=100, null=True, blank=True)
    key2= models.CharField(max_length=100, null=True, blank=True)
    key3= models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shortcut_name 