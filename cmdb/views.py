# Create your views here.
# 用于跳转页面
from django.core import serializers
from django.shortcuts import render
# 返回值载体
from django.shortcuts import HttpResponse
# Model对象
# TODO MVP分层存在问题
from cmdb import models
# JSON支持
import json


# 打印HelloWord
def helloWord(request):
	return HttpResponse("Hello Word!")


# 跳转index页面
def index(request):
	return render(request, 'index.html')


# 提交表单
def submit(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		print(username, password)
	return HttpResponse('username=' + username + ", password=" + password)


# 搜索数据
def query(request):
	orderCode = request.GET.get("orderCode", None)
	list = []

	if orderCode != None:
		list = models.MyTask.objects.filter(order_code=orderCode)
	return HttpResponse(serializers.serialize('json', list), 'application/json')
