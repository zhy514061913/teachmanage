from collections import OrderedDict
from pymongo.response import Response
from rest_framework.pagination import PageNumberPagination


class StandarPagination(PageNumberPagination):
    page_size = 20  # 默认每页显示条数配置
    page_query_param = 'page'  # “页数”的请求参数名称, 默认是page
    page_size_query_param = 'page_size'  # “分页大小”的请求参数名称

    # 进入父类 PageNumberPagination 可看响应体返回字段.
    #  def get_paginated_response(self, data):
    #  return Response(OrderedDict([
    #    ('count', self.page.paginator.count),
    #    ('next', self.get_next_link()),
    #    ('previous', self.get_previous_link()),
    #    ('results', data)
    #  ]))

    # 觉得不适用, 那就拷贝出来,重载函数, 自己多加几个字段.
    # (可通过官方文档或直接调试得知从哪些属性获取正确的值.)
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('page', self.page.number),
            ('total_page', self.page.paginator.num_pages),
            ('page_size', self.page.paginator.per_page),
            ('results', data)
        ]))

# class Pagination(object):
#     """自定义分页（Bootstrap版）"""
#
#     def __init__(self, current_page, total_count, base_url, per_page=10, max_show=11):
#         """
#         :param current_page: 当前请求的页码
#         :param total_count: 总数据量
#         :param base_url: 请求的URL
#         :param per_page: 每页显示的数据量，默认值为10
#         :param max_show: 页面上最多显示多少个页码，默认值为11
#         """
#         try:
#             self.current_page = int(current_page)
#         except Exception as e:
#             # 取不到或者页码数不是数字都默认展示第1页
#             self.current_page = 1
#         # 定义每页显示多少条数据
#         self.per_page = per_page
#         # 计算出总页码数
#         total_page, more = divmod(total_count, per_page)
#         if more:
#             total_page += 1
#         self.total_page = total_page
#         # 定义页面上最多显示多少页码(为了左右对称，一般设为奇数)
#         self.max_show = max_show
#         self.half_show = max_show // 2
#         self.base_url = base_url
#
#     @property
#     def start(self):
#         return (self.current_page - 1) * self.per_page
#
#     @property
#     def end(self):
#         return self.current_page * self.per_page
