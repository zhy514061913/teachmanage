# Create your views here.
from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import action

from common.CustomViewBase import CustomViewBase
from apps.user import serializers
from apps.user.filters import UsersFilter
from apps.user.models import User




class goodsList(CustomViewBase):
    # 查询所有信息
    queryset = User.objects.order_by('-id')
    # 序列化
    serializer_class = serializers.UserSerializer
    data = serializer_class.data
    search_fields = ('name', 'password')
    filterset_class = UsersFilter


class GoodViewSet(CustomViewBase):
    # throttle_classes = (UserRateThrottle, AnonRateThrottle)
    # serializer_class = serializers.UserSerializer
    # queryset = User.objects.all()
    #
    # # 设置列表页的单独auth认证也就是不认证
    # # authentication_classes = (TokenAuthentication,)
    #
    # # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # # 设置排序
    # ordering_fields = ('id', 'name')
    # # 设置filter的类为我们自定义的类
    # filter_class = UsersFilter
    # # 设置我们的search字段
    # search_fields = ('name', 'id', 'password')

    def get_object(self):
        return self.request.user

    # 商品点击数+1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = '3333'
        instance.save()
        serializer = self.get_serializer(instance)
        return JsonResponse(serializer.data)

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        '''
        账号密码登录
        '''
        data = request.data
        serializer = self.get_serializer(data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response()

    @action(methods=['get'], detail=False)
    def info(self, request):
        """
       用户详情
       """
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
