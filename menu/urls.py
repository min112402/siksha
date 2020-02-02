from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from menu import views

router = routers.DefaultRouter()
router.register(r'menus', views.MenuViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
]

