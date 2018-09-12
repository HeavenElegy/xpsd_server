from apps.workAssistant.service import common


# 登录请求
from django.http import HttpResponse


def login(requset):
    return common.login(requset)