from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tipos', TiposDatosViewset)


# router.register('users', views.UserViewSet)
# router.register('groups', views.GroupViewSet)

app_name = 'principal'
urlpatterns = [
    path('', index, name='index'),

    path('api/', include(router.urls)),

]
