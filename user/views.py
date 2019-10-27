# 不用模板
# Create your views here.
import logging

import simplejson
from django.core import serializers
from django.core.paginator import Paginator
from django.core.serializers import json
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse

from utils import HttpCode
from .models import User
from django.forms.models import model_to_dict
from django.shortcuts import render


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
                return HttpCode.result(200, "success", model_to_dict(user))
            except Exception as e:
                print('异常了')
                raise
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()


def pageList(request: HttpRequest):
    print("查询访问接口成功")
    try:
        # 固定用法，获取用户想访问的当前页 123
        #userList = User.objects.values()
        # json_data = serializers.serialize("json", userList)
        # user_list = User.objects.values().filter(id=1)
        user_list = User.objects.values().filter(id=1)
        Paginator(user_list,)
        print("111", list(user_list))
        return JsonResponse(list(user_list))
        # print("222", json.loads(json_data))
        # print("222",json_data)

        # .values()结果如何序列化为json？
        #
        # （1）将QuerySet转为list: city_list = list(cities)
        #
        # （2）将list序列化为json: city_json = json.dumps(city_list)


        # 实例化分页器对象
        # page=request.GET.get('page',1)
        # page_obj = Pagination(current_page=page,all_count=book_queryset.count(),per_page_num=10)
        # page_queryset = book_queryset[page_obj.start:page_obj.end]

    except Exception as e:
        print("异常了")
        logging.info(e)
        return HttpResponseBadRequest()
