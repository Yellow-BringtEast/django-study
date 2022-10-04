from django.shortcuts import render, redirect
from web_crm import models


# Create your views here.
def department_list(request):
    """部门列表"""
    # 去数据库中获取所有的部门信息
    depart_list = models.Department.objects.all()

    return render(request, 'depart_list.html', {'depart_list': depart_list})


def department_add(request):
    """添加部门 """
    if request.method == 'GET':
        return render(request, 'depart_add.html')

    # 获取用户通过POST提交的数据
    title = request.POST.get('title')

    # 保存到数据库
    models.Department.objects.create(title=title)

    # 重定向会部门管理页面
    return redirect('/department/list/')


def department_delete(request):
    """删除部门 """
    # 获取需删除的id
    nid = request.GET.get('nid')

    # 删除数据
    models.Department.objects.filter(id=nid).delete()

    # 重定向会部门管理页面
    return redirect('/department/list/')


def department_edit(request, nid):
    """编辑部门"""
    if request.method == 'GET':
        # 获取nid对应的部门
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_object': row_object})

    # 获取修改后的部门名称
    title = request.POST.get('title')

    # 根据id修改部门名称
    models.Department.objects.filter(id=nid).update(title=title)

    # 重定向会部门管理页面
    return redirect('/department/list/')

