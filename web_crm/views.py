from django.shortcuts import render, HttpResponse, redirect
from .models import Department


# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    # 1.去app目录下的templates文件夹寻找对应的html文件
    return render(request, 'user_list.html')


def tpl(request):
    name = 'hello world'
    role = ['你', '好', '世界']
    user_info = {'name': 'guojia', 'salary': 500, 'role': 'ceo'}

    data_list = [
        {'name': 'guojia', 'salary': 500, 'role': 'ceo'},
        {'name': 'nihao', 'salary': 600, 'role': 'ceo'},
        {'name': 'xiexie', 'salary': 700, 'role': 'ceo'}
    ]
    return render(request, 'tpl.html', {'n1': name, 'n2': role, 'n3': user_info, 'n4': data_list})


def something(request):
    # request是一个对象，封装了用户通过浏览器发送给服务器的所有请求相关的数据
    # 获取用户的请求方式 GET/POST
    print(request.method)

    # 用户请求url上的传递值 /something/?n1=123&n2=999
    print(request.GET)

    # 获取请求体中传递的参数
    print(request.POST)

    # 三种常见的响应：HttpResponse、render、redirect(重定向)

    return HttpResponse('XXXX')


def login(request):
    # 如果请求方式为GET，则直接返回html页面给用户
    if request.method == 'GET':
        return render(request, 'login.html')

    # 如果请求方式为POST，则获取用户提交的数据，进行业务逻辑处理
    username = request.POST.get('user')
    password = request.POST.get('pwd')

    # 账号密码校验
    if username == 'root' and password == '123':
        return redirect('https://www.baidu.com')

    # 校验失败返回登录页面并提示错误信息
    return render(request, 'login.html', {'error_message': '用户名或密码错误'})


def orm(request):
    # 测试ORM操作表中的数据
    Department.objects.create(title='销售部')
    Department.objects.create(title='IT')
    Department.objects.create(title='运营部')

    return HttpResponse('成功')