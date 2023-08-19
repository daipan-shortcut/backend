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