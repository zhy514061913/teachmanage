# 不用模板
# Create your views here.
import logging

import simplejson
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from common.CustomViewBase import CustomViewBase
from user.filters import UsersFilter
from . import serializers
from .models import User


# page_size 每页数目
# page_query_param 前端发送的页数关键字名，默认为"page"
# page_size_query_param 前端发送的每页数目关键字名，默认为None
# max_page_size 前端最多能设置的每页数量
# class DefaultPagination(PageNumberPagination):
#     page_size_query_param = 'page_size'
#     max_page_size = 10
#
#
# class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer
#     page = DefaultPagination()
#     pagination_class = DefaultPagination


class userList(CustomViewBase):
    # 查询所有信息
    queryset = User.objects.order_by('-id')
    # 序列化
    serializer_class = serializers.UserSerializer
    data = serializer_class.data
    search_fields = ('name', 'password')
    filterset_class = UsersFilter


class UserViewSet(CustomViewBase):
    @action(methods=['get'], detail=False)
    def info(self, request, *args, **kwargs):
        """
        用户详情
        """
        instance = self.get_object()
        print('instance', instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RegApi(APIView):
    @api_view(['POST'])
    def cheakmail(request):
        return HttpResponse()

    def reg(request: HttpRequest):
        print("访问接口成功")
        try:
            payload = simplejson.loads(request.body.decode())
            email = payload['email']
            # 看看数据库中有没有email
            qs = User.objects.filter(email=email)  # 列表[]
            if qs:  # qs != null
                print('1')
                return HttpResponseBadRequest()
            else:
                name = payload['username']
                password = payload['password']
                user = User()
                user.name = name
                user.email = email
                user.password = password
                try:
                    user.save()
                    print('json111', type(user))
                    print('json222',
                          user.__dict__)  # model转字典  {'_state': <django.db.models.base.ModelState object at 0x04FC9590>, 'id': 21, 'name': 'zhangsan', 'email': '1@qq.com', 'password': '123456'}
                    print('json222', model_to_dict(
                        user))  # model转字典{'id': 21, 'name': 'zhangsan', 'email': '1@qq.com', 'password': '123456'}
                    # return JsonResponse(model_to_dict(user))  # 200
                    # results={}
                    # results['date']=model_to_dict(
                    #     user)
                    # results['status_code']=200
                    # return JsonResponse(results, safe=False)
                    # return HttpCode.result(200, "success", model_to_dict(user))
                except Exception as e:
                    print('异常了')
                    raise
        except Exception as e:
            logging.info(e)
            return HttpResponseBadRequest()
