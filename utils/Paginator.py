class Pagination(object):
    """自定义分页（Bootstrap版）"""

    def __init__(self, current_page, total_count, base_url, per_page=10, max_show=11):
        """
        :param current_page: 当前请求的页码
        :param total_count: 总数据量
        :param base_url: 请求的URL
        :param per_page: 每页显示的数据量，默认值为10
        :param max_show: 页面上最多显示多少个页码，默认值为11
        """
        try:
            self.current_page = int(current_page)
        except Exception as e:
            # 取不到或者页码数不是数字都默认展示第1页
            self.current_page = 1
        # 定义每页显示多少条数据
        self.per_page = per_page
        # 计算出总页码数
        total_page, more = divmod(total_count, per_page)
        if more:
            total_page += 1
        self.total_page = total_page
        # 定义页面上最多显示多少页码(为了左右对称，一般设为奇数)
        self.max_show = max_show
        self.half_show = max_show // 2
        self.base_url = base_url

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page

    @property
    def end(self):
        return self.current_page * self.per_page
