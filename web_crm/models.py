from django.db import models


# Create your models here.
# 建表：
# 1.新建类-类名：表名  属性：字段名
# 2.在命令行中依次执行： python manage.py makemigrations
#                    python manage.py migrate

# 增删改查
# 1.insert
# Department.objects.create(title='销售部')
# 2.delete
# Department.objects.filter(id=3).delete()
# 3.select
# Department.objects.all() - QuerySet类型的对象列表
# 4.update
# Department.objects.all().update()

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


class Department(models.Model):
    title = models.CharField(max_length=16)
