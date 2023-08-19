from django.shortcuts import render
from django.db import IntegrityError
from django.db.models import Q
from datetime import date, datetime
from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .utils.auth import JWTAuthentication, NormalAuthentication
from django.http import Http404

from .models import *
from .serializers import *

class shortcutViewSet(generics.ListAPIView):
    queryset = shortcut.objects.order_by('shortcut_id')
    serializer_class = shortcutSerializer
    permission_classes = (AllowAny,)


class keymapViewSet(generics.ListCreateAPIView):
    queryset = keymap.objects.all()
    serializer_class = keymapSerializer
    permission_classes = (AllowAny,)

class shortcutsortViewSet(generics.ListAPIView):
    serializer_class = shortcutSerializer

    def get_queryset(self):
        f_os = self.kwargs['f_os']
        if f_os == 'Windows':
            f_os = 1
        if f_os == 'Mac':
            f_os = 2
        if f_os == 'Linux':
            f_os = 3

        return shortcut.objects.filter(f_os=f_os).order_by('shortcut_id')

#ユーザー関連
class Login(APIView):

    authentication_classes = [NormalAuthentication,]

    def post(self, request, *args, **kwargs):
        return Response({"token": request.user})

#post PUT、PATCH
class userregisterSet(generics.CreateAPIView):
    queryset = t_user.objects.all()
    serializer_class = t_userSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
        except IntegrityError:
            # error_response = Response({"error": "既に登録されています。"})
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return response

class userViewSet(generics.RetrieveUpdateAPIView):
    queryset = t_user.objects.all()
    serializer_class = t_userSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

class remenderlistViewSet(generics.CreateAPIView):
    queryset = remember_shortcut.objects.all()
    serializer_class = remember_shortcutpostSerializer
    # authentication_classes = [JWTAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    permission_classes = (AllowAny,)

class remenderViewSet(generics.RetrieveAPIView):
    serializer_class = remember_shortcutSerializer
    lookup_field = 'remember_shortcut_id'

    def get_queryset(self):
        f_user = self.kwargs['f_user']
        f_os = self.kwargs['f_os']
        if f_os == 'Windows':
            f_os = 1
        if f_os == 'Mac':
            f_os = 2
        if f_os == 'Linux':
            f_os = 3
        return remember_shortcut.objects.filter(f_user=f_user, f_os=f_os)

    def get_object(self):
        queryset = self.get_queryset()
    #remember_shortcut_idがいちばん大きいものを取得
        obj = queryset.order_by('-remember_shortcut_id').first()
    
        if obj is None:
            raise Http404("No object found matching this query.")
        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    permission_classes = (AllowAny,)


class arrivalView(APIView):
    def get(self, request, f_user):
        #各OSのショートカット数を取得
        windows = shortcut.objects.filter(f_os=1).count()
        mac = shortcut.objects.filter(f_os=2).count()
        linux = shortcut.objects.filter(f_os=3).count()

        #各OSのユーザーのミスショートカット数を取得
        try:
            misswindows = remember_shortcut.objects.filter(f_user=f_user, f_os=1).order_by('-remember_shortcut_id').first().shortcuts.count()
        except AttributeError:
            misswindows = 0
        try:
            missmac = remember_shortcut.objects.filter(f_user=f_user, f_os=2).order_by('-remember_shortcut_id').first().shortcuts.count()
        except AttributeError:
            missmac = 0
        try:    
            misslinux = remember_shortcut.objects.filter(f_user=f_user, f_os=3).order_by('-remember_shortcut_id').first().shortcuts.count()
        except AttributeError:
            misslinux = 0
        
        if windows == 0:
            arrivalwindows = 0
        else:
            arrivalwindows = round((windows - misswindows) / windows * 100)
        
        if mac == 0:
            arrivalmac = 0
        else:
            arrivalmac = round((mac - missmac) / mac * 100)
        
        if linux == 0:
            arrivallinux = 0
        else:
            arrivallinux = round((linux - misslinux) / linux * 100)
        return Response({
            'question':{
            'Windows': windows,
            'Mac': mac,
            'Linux': linux,
            },
            'missanswer':{
            'Windows': misswindows,
            'Mac': missmac,
            'Linux': misslinux,
            },
            'arrival':{
            'Windows': arrivalwindows,
            'Mac': arrivalmac,
            'Linux': arrivallinux,
            },

        })
    
    permission_classes = (AllowAny,)