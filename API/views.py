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
import random

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

        queryset = shortcut.objects.filter(f_os=f_os).order_by('shortcut_id')
        return random.sample(list(queryset), min(len(queryset), 10))

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

class successlistViewSet(generics.CreateAPIView):
    queryset = success_shortcut.objects.all()
    serializer_class = success_shortcutpostSerializer
    # authentication_classes = [JWTAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
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
            misswindows = None
        try:
            missmac = remember_shortcut.objects.filter(f_user=f_user, f_os=2).order_by('-remember_shortcut_id').first().shortcuts.count()
        except AttributeError:
            missmac = None
        try:    
            misslinux = remember_shortcut.objects.filter(f_user=f_user, f_os=3).order_by('-remember_shortcut_id').first().shortcuts.count()
        except AttributeError:
            misslinux = None
        
        #各OSのユーザーの正解ショートカット数を取得
        try:
            successwindows = success_shortcut.objects.filter(f_user=f_user, f_os=1).order_by('-succsess_shortcut_id').first().shortcuts.count()
        except AttributeError:
            successwindows = None
        try:
            successmac = success_shortcut.objects.filter(f_user=f_user, f_os=2).order_by('-succsess_shortcut_id').first().shortcuts.count()
        except AttributeError:
            successmac = None
        try:
            successlinux = success_shortcut.objects.filter(f_user=f_user, f_os=3).order_by('-succsess_shortcut_id').first().shortcuts.count()
        except AttributeError:
            successlinux = None
        
        #各OSのユーザーの正解率を取得
        if windows == 0:
            arrivalwindows = None
        elif successwindows is None:
            arrivalwindows = None
        else:
            arrivalwindows = round(successwindows / windows * 100)
        if mac == 0:
            arrivalmac = None
        elif successmac is None:
            arrivalmac = None
        else:
            arrivalmac = round(successmac / mac * 100)
        if linux == 0:
            arrivallinux = None
        elif successlinux is None:
            arrivallinux = None
        else:
            arrivallinux = round(successlinux / linux * 100)
        
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
            'successanswer':{
            'Windows': successwindows,
            'Mac': successmac,
            'Linux': successlinux,
            },
            'arrival':{
            'Windows': arrivalwindows,
            'Mac': arrivalmac,
            'Linux': arrivallinux,
            },

        })
    
    permission_classes = (AllowAny,)