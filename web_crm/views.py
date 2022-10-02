from django.shortcuts import render, HttpResponse
import requests


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
