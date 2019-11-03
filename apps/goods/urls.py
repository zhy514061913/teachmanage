from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'goodList', views.goodsList)
router.register(r'goodview', views.GoodViewSet, base_name='goodview')

urlpatterns = router.urls
