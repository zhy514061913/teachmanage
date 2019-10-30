#Django采用MVC架构设计的开源的WEB快速开发框架

Django生命周期概括:

    前端发送请求-->Django的wsgi-->中间件-->路由系统-->视图-->ORM数据库操作-->模板-->返回数据给用户

rest framework生命周期：

    前端发送请求-->Django的wsgi-->中间件-->路由系统_执行CBV的as_view()，就是执行内部的dispath方法-->在执行dispath之前，有版本分析 和 渲染器-->在dispath内，对request封装-->版本-->认证-->权限-->限流-->视图-->如果视图用到缓存( request.data or   request.query_params )就用到了 解析器-->视图处理数据，用到了序列化(对数据进行序列化或验证) -->视图返回数据可以用到分页
    
###优点：
> 能够快速开发，如Auth,Cache，模板
MVC设计模式
实用的管理后台
自带ORM，Template,Form,Auth核心
组件
简介的url设计
周边插件丰富

###缺点
> 重，因为东西大而全
同步阻塞

所以Django的设计目标就是一款大而全，便于企业快捷开发项目的框架，
因此应用广泛

###Django安装
  ```
$ pip install django == 1.11
$ django-admin(帮助命令)
$ pip show django(查看django版本)
  ``` 
###创建项目
```
$ django-admin startproject 项目名 .  (点的意义是不需要重复的创建文件夹，如果不加点，会在项目包外再自动创建一个同名文件夹)
``` 
### 重要文件说明
> manage.py : 本项目管理的命令行工具，应用创建，数据库迁移等，都使用它完成。
>blog/settings.py ：本项目的配置文件。数据库参数等
>blog/urls.py ：url路径映射配置。默认情况下，只配置/admin的路由
>blog/wsgi ：定义WSGI接口信息，一般无须改动


###数据库连接
> Django支持MySQL5.5+
>Django官方推荐使用本地驱动mysqlclient 1.3.7+

```
$ pip install mysqlclient
```

>windows下安装错误解决方法
> error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
>为编译环境问题 
>1.下载Visual C++ Redistributable Packages 2015、2017安装，但是即使安装后
>确实看到了V14库，也不保证安装mysqlclient就成功
>2.直接安装编译好的wheel文件
>到https://www.lfd.uci.edu/~gohlke/pythonlibs/ 下载对应python版本的mysqlclient-1.4.4-cp37-cp37m-win_amd64文件
```
$ pip install "mysqlclient-1.4.4-cp37-cp37m-win_amd64.whl"
```
>如果ERROR: mysqlclient-1.4.4-cp37-cp37m-win_amd64.whl is not a supported wheel on this platform.
>可以选择mysqlclient-1.4.4-cp37-cp37m-win32.whl下载


###项目开始
> 1.查看django的所有命令
```
$ python manage.py
```

>2.创建应用
```
$ python manage.py startapp user
```
>在setting文件中 _INSTALLED_APPS_ 注册新建模块
>创建应用后，在项目的更目录下产生一个user目录，有如下文件：

>1.admin.py 管理站点模型的声明文件
>2.moudels.py 模型层Model类定义
>3.view.py 定义URL响应函数
>4.migrations包 数据迁移文件生成目录
>5.apps.py 应用的信息定义文件


###迁移Migration
>迁移：从模型定义生成数据库表
>1.生成迁移文件
```
$python manage.py makemigrations

Migratins for 'user'
    user\migrations\0001_initial.py
    -Create model User

生成如下文件
user
    migrations 
        0001_inital.py
        __init__.py

```
>修改过Model类，还需调用makemigrations吗？
>还是节制migrate?总之序号会增加
>注意： 迁移的应用必须在setting.py的INSTALLED_APPS中注册


##后台管理
###1.创建管理员
>管理员用户名 admin
>密码 admin123
```
$ python manage.py createsuperuser

```
###2.本地化
>settings.py中设置语言、时区

###3.启动WebServer
```
python manage.py runserver
```
>默认启动 8000 端口

>注册应用模块
>在user应用的admin.py添加
``` 
from user.models import User

admin.site.register(User)#注册

```

##模板
>如果使用react实现前端页面，其实Django就没有必须要使用模板，它其实就是一个后台服务程序
>接收请求，响应数据。接口设计就可以是纯粹的Restful风格
>
>模板的目的是可视化，将数据按照一定布局格式输出，而不是为了数据处理，所以
>一般不会有复杂的处理逻辑，模板的引入实现了业务逻辑和显示格式的分离，
>这样，在开发中，就可以分工协作，页面开发完成页面布局设计，后台开发完成数据处理逻辑的实现
>
>Python的模板引擎默认使用Django template languange(DTL)构建
>

#FAQ
##如果与到跨域问题，怎么办？
>首先在安装
```
pip install django-cors-headers
```
>注册应用
```
INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)
```
>配置settings.py文件
```

INSTALLED_APPS = [
    ...
    'corsheaders'，
    ...
 ] 
 
MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', # 注意顺序
    ...
)
#跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)
 
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
 
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
```
>按照这个配置配置完就好使了
>如果在有问题，检查请求头的内容，例如token


##关于中间件
>有的时候我们会在页面中展示大量数据，全部都放在一页可能会降低用户体验，Django提供了一个Paginator类来帮助我们管理分页数据。
>

