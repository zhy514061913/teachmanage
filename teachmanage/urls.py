"""teachmanage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader, RequestContext


# 不同的业务，要对应到对应的url映射上 --为了简明，使用多级路由
# 模板
# def index(request):
#     print(request)
#     print(type(request))
#     return render(request, 'index.html', {'user': 'helloword'})  # html str
# return JsonResponse({'user':'helloword'})#json str
# 源代码
# def index1(request):
#     print(request)
#     print(type(request))
#     tem = loader.get_template('index.html')  # 加载器模块搜索模板并加载它
#     context = RequestContext(request, {'content': '123'})
#     return HttpResponse(tem.render(context))
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

