# -*- coding: utf-8 -*-
# author:laoseng(QQ:1572665580),feilong(hhr66@qq.com)
# create:2018-09
#  查询过滤条件

from django_filters import rest_framework as filters
from apps.user.models import User


class UsersFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = ('name', 'id', 'email','password')

