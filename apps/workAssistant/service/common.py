# -*- coding: utf-8 -*-

import json
from builtins import print
from django.http import HttpResponse
from apps.workAssistant.entities import entity
from django.views.decorators.http import require_http_methods

from apps.workAssistant.utils import encryption
from apps.workAssistant.entities.base import BaseResponse


@require_http_methods(["POST"])
def login(request):

    username = request.POST.get("username", None)
    password = request.POST.get("password", None)

    if username == None or password == None:
        return HttpResponse("参数异常")

    # 查询用户数据
    userlist = entity.User.objects.filter(login_name=username)
    count = userlist.count()
    if count == 0:
        return BaseResponse('01', "账户或密码错误")
    elif count >1:
        return BaseResponse('02', "result > 2")

    user = userlist[0]
    print(type(user))
    print(user)

    password = user.password
    ePassword = encryption.resolvePassword(password)
    if password != ePassword:
        return BaseResponse('01', "账户或密码错误")


    return {"msg": "哈~"}