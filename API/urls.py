from django.urls import path
from . import views

urlpatterns = [
    path('shortcut/', views.shortcutViewSet.as_view()),
    path('shortcut/<int:f_os>/', views.shortcutsortViewSet.as_view()),
    path('keymap/', views.keymapViewSet.as_view()),
    path('userregister/', views.userregisterSet.as_view()),
    path('login/', views.Login.as_view()),
]