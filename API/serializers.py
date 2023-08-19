from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import *
from rest_framework.serializers import ModelSerializer

class osSerializer(serializers.ModelSerializer):
    class Meta:
        model = os
        fields = [
            # 'os_id',
            'os_name',
        ]

class keymapSerializer(serializers.ModelSerializer):
    class Meta:
        model = keymap
        fields = [
            # 'keymap_id',
            'key',
            'placeholder',
        ]
class shortcutSerializer(serializers.ModelSerializer):
    os = SerializerMethodField()
    key1 = SerializerMethodField()
    key2 = SerializerMethodField()
    key3 = SerializerMethodField()
    class Meta:
        model = shortcut
        fields = [
            'shortcut_id',
            'shortcut_name',
            'os',
            'key1',
            'key2',
            'key3',
        ]
    
    def get_os(self, obj):
        try:
            os__abstruct_contents = osSerializer(os.objects.all().filter(os_id=obj.f_os.os_id), many=True).data
            return os__abstruct_contents
        except:
            return None
    def get_key1(self, obj):
        try:
            key1__abstruct_contents = keymapSerializer(keymap.objects.all().filter(keymap_id=obj.f_key1.keymap_id), many=True).data
            return key1__abstruct_contents
        except:
            return None
    def get_key2(self, obj):
        try:
            key2__abstruct_contents = keymapSerializer(keymap.objects.all().filter(keymap_id=obj.f_key2.keymap_id), many=True).data
            return key2__abstruct_contents
        except:
            return None
    def get_key3(self, obj):
        try:
            key3__abstruct_contents = keymapSerializer(keymap.objects.all().filter(keymap_id=obj.f_key3.keymap_id), many=True).data
            return key3__abstruct_contents
        except:
            return None
        
class t_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = t_user
        fields = [
            'user_id',
            'email',
            'password',
        ]
#外部キーから参照するよう
class t_userSerializerfor(serializers.ModelSerializer):
    class Meta:
        model = t_user
        fields = [
            'user_id',
            'email',
        ]