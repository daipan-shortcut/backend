from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import *
from rest_framework.serializers import ModelSerializer

class osSerializer(serializers.ModelSerializer):
    class Meta:
        model = os
        fields = [
            'os_id',
            'os_name',
        ]

class shortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = shortcut
        fields = [
            'shoortcut_id',
            'shortcut_name',
            'f_os',
            'key1',
            'key2',
            'key3',
            'os'
        ]
    
    def get_os(self, obj):
        try:
            os__abstruct_contents = osSerializer(os.objects.all().filter(os_id=obj.f_os.os_id), many=True).data
            return os__abstruct_contents
        except:
            return None