from django.shortcuts import render
from django.db import IntegrityError
from django.db.models import Q
from datetime import date, datetime
from rest_framework import generics, filters, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

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

