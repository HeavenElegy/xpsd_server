import json

from django.http import HttpResponse
from django.test import RequestFactory
from django.utils.deprecation import MiddlewareMixin


# 登录拦截器
from system.authentication import AES


class LoginInterceptor(MiddlewareMixin):
    """
    登陆拦截器
    """
    def process_request(self, request):
        if needLogin(request):
            return HttpResponse("需要登录")

    def process_response(self, request, response):
        return response


class AuthenticationInterceptor(MiddlewareMixin):
    """
    鉴权拦截器
    """

    def process_request(self, request):
        # 1. 判断是否需要鉴权
        # 1.1. 根据情况进行鉴权
        if needAuthentication(request):
            return HttpResponse("鉴权失败")


    def process_response(self, request, response):
        return response


def needLogin(request):
    """
    判断是否需要登录
    :param request:
    :return:
    """
    path = request.path
    session = request.session.get('user', None)
    if path != '/login/' and session == None:
        return True
    else:
        return False


def needAuthentication(request):
    """
    判断是否需要鉴权
    :param request:
    :return:
    """
    path = request.path
    session = request.session.get('user', None)
    if path != '/login/' and session == None:
        return True
    else:
        return False


def needDecrypt(request):
    """
    判断是否需要解密
    :param request:
    :return:
    """
    path = request.path
    session = request.session.get('user', None)
    return True

def decrypt(request):
    """
    解密
    :param request:
    :return:
    """
    method = request.method
    global ay
    if method == "GET":
        # get请求
        ay = request.GET.get("ay")
    elif method == "POST":
        # post请求
        ay = request.POST.get("ay")
    try:
        return AES.decryptToString(ay)
    except BaseException as e:
        print(e.__str__())


class ConfusionInterceptor(MiddlewareMixin):
    """
    混淆
    """
    def process_request(self, request):
        global ciphertext
        global body
        method = request.method
        if method == "GET":
            body = request.GET = request.GET.copy()
        elif method == "POST":
            body = request.POST = request.POST.copy()


        # 1. 判断是否需要解密
        # 1.1. 根据情况进行解密
        if needDecrypt(request):
            ciphertext = decrypt(request)
            if ciphertext == None:
                return HttpResponse("参数异常")
            else:
                jsonn = json.loads(ciphertext)
                for j in jsonn:
                    body[j] = jsonn.get(j)

    def process_response(self, request, response):
        return response

