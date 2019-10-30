# !/usr/bin/env python
# -*- coding:utf-8 -*-
from django.http import JsonResponse


class HttpCode(object):
    ok = 200
    paramserror = 400
    unantu = 401
    methoderror = 405
    servererror = 500


def ok():
    return result()


# def result(code=HttpCode.ok, message='', data=None, kwargs=None):
#     print('json_dict')
#     json_dict = {'code': code, 'message': message, 'data': data}
#     if kwargs and isinstance(kwargs, dict) and kwargs.keys():
#         json_dict.update(kwargs)
#     print('json_dict'.json_dict)
#     return JsonResponse(json_dict)

# def resultPage(code=HttpCode.ok, message='', data=None, total=0):
#     json_dict = {'code': code, 'message': message, 'data': data, 'total': total}
#     # print('json_dict', json_dict)
#     return HttpResponse(json_dict)


def result(code=HttpCode.ok, message='', data=None):
    json_dict = {'code': code, 'message': message, 'data': data}
    print('json_dict', json_dict)
    return JsonResponse(json_dict)


def params_error(message='', data=None):
    return result(code=HttpCode.paramserror, message=message, data=data)


def unauth(message='', data=None):
    return result(code=HttpCode.unantu, message=message, data=data)


def method_error(message='', data=None):
    return result(code=HttpCode.methoderror, message=message, data=data)


def server_error(message='', data=None):
    return result(code=HttpCode.servererror, message=message, data=data)
