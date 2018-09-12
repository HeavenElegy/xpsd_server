from builtins import print
from django.http import HttpResponse
from apps.workAssistant.entities import entity
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def login(request):

    username = request.POST.get("username", None)
    password = request.POST.get("password", None)

    print(request.body)

    if username == None or password == None:
        return HttpResponse("参数异常")

    # 查询用户数据
    userlist = entity.User.objects.filter(login_name=username)
    count = userlist.count()
    if count == 0:
        return HttpResponse("登录失败")
    elif count >1:
        return HttpResponse("result > 2")

    # 查找完成
    print("检视OK")
    return HttpResponse("检视OK")
