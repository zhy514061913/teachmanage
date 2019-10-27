from django.conf.urls import url
from .views import reg
from .views import pageList

urlpatterns = [
    url(r'^reg$', reg),
    url(r'^pageList$', pageList)
]
