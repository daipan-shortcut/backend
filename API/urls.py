from django.urls import path
from . import views

urlpatterns = [
    path('shortcut/', views.shortcutViewSet.as_view()),
    path('shortcut/<str:f_os>/', views.shortcutsortViewSet.as_view()),
    path('keymap/', views.keymapViewSet.as_view()),
    path('userregister/', views.userregisterSet.as_view()),
    path('login/', views.Login.as_view()),
    path('remember/', views.remenderlistViewSet.as_view()),
    path('remember/<int:f_user>/<str:f_os>/', views.remenderViewSet.as_view()),
    path('success/', views.successlistViewSet.as_view()),
    path('arrival/<str:f_user>/', views.arrivalView.as_view()),
    path('shortcutdetail/<int:pk>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/<int:pk3>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/<int:pk3>/<int:pk4>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/<int:pk3>/<int:pk4>/<int:pk5>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/<int:pk3>/<int:pk4>/<int:pk5>/<int:pk6>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/<int:pk3>/<int:pk4>/<int:pk5>/<int:pk6>/<int:pk7>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/<int:pk3>/<int:pk4>/<int:pk5>/<int:pk6>/<int:pk7>/<int:pk8>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/<int:pk3>/<int:pk4>/<int:pk5>/<int:pk6>/<int:pk7>/<int:pk8>/<int:pk9>/', views.shortcutdetailViewSet.as_view()),
    path('shortcutdetail/<int:pk>/<int:pk2>/<int:pk3>/<int:pk4>/<int:pk5>/<int:pk6>/<int:pk7>/<int:pk8>/<int:pk9>/<int:pk10>/', views.shortcutdetailViewSet.as_view()),
]