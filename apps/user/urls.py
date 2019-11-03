from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'userList', views.userList)
router.register(r'userview', views.UserViewSet, base_name='userview')

urlpatterns = router.urls
