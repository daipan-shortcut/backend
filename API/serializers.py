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
    f_os = serializers.StringRelatedField()
    f_key1 = keymapSerializer()
    f_key2 = keymapSerializer()
    f_key3 = keymapSerializer()
    class Meta:
        model = shortcut
        fields = [
            'shortcut_id',
            'shortcut_name',
            'f_os',
            'f_key1',
            'f_key2',
            'f_key3',
        ]

        
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

class remember_shortcutpostSerializer(serializers.ModelSerializer):

    class Meta:
        model = remember_shortcut

        fields = [
            'remember_shortcut_id',
            'f_user',
            'f_os',
            'shortcuts',
        ]

class remember_shortcutSerializer(serializers.ModelSerializer):
    shortcuts = shortcutSerializer(many=True)
    f_os = serializers.StringRelatedField()
    class Meta:
        model = remember_shortcut

        fields = [
            'f_os',
            'shortcuts',
        ]

class success_shortcutpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = success_shortcut
        fields = [
            'succsess_shortcut_id',
            'f_user',
            'f_os',
            'shortcuts',
        ]