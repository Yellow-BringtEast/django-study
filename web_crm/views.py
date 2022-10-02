from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')


def user_list(request):
    # 1.去app目录下的templates文件夹寻找对应的html文件
    return render(request, 'user_list.html')
