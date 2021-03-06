"""connectoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from account.api import AccountViewSet, RoleViewSet, RegisterAPI, user_id_api
from connectoon.HybridRouter import HybridRouter

router = HybridRouter()
router.register('role', viewset=RoleViewSet)
router.register('account', viewset=AccountViewSet)
router.add_api_view('register', path('register/', RegisterAPI.as_view(), name='register'))
router.add_api_view('token', path('token/', obtain_auth_token, name='get-token'))
router.add_api_view('user-id', path('user-id/', user_id_api, name='get-user-id'))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
