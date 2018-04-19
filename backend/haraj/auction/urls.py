from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register('register', views.userCreate, base_name=views.userCreate)

urlpatterns = router.urls