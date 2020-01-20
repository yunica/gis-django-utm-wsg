from django.urls import path, include
from .views import *
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('tipos', TiposDatosViewset)


# router.register('users', views.UserViewSet)
# router.register('groups', views.GroupViewSet)

app_name = 'principal'
urlpatterns = [
    path('', index, name='index'),
    path('utm', TemplateView.as_view(template_name="vscod/input.html"), name='utm'),

    path('api/', include(router.urls)),

]
