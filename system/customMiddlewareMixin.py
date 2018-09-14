import json
import array

from django.http import HttpResponse
from django.test import RequestFactory
from django.utils.deprecation import MiddlewareMixin
from django.core import serializers
from apps.workAssistant.support.jsonSupport import CustomJsonEncoder
from system.authentication import AES


# 这里的所有拦截器的process_request与process_response方法的调用顺序为q1->q2->q3->p3->p2->p1
class LoginInterceptor(MiddlewareMixin):
    """
    登陆拦截器
    """
    def process_request(self, request):
        if needLogin(request):
            return HttpResponse("需要登录")

    def process_response(self, request, response):
        return response


class TransitionInterceptor(MiddlewareMixin):
    """
    转换拦截器
    """
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if isinstance(response, HttpResponse):
            return response
        else:
            return HttpResponse(json.dumps(response, cls=CustomJsonEncoder).encode('utf-8').decode('unicode_escape'), "application/json;charset=UTF-8")

class AuthenticationInterceptor(MiddlewareMixin):
    """
    鉴权拦截器
    """

    def process_request(self, request):
        # 1. 判断是否需要鉴权
        # 1.1. 根据情况进行鉴权
        if needAuthentication(request):
            return HttpResponse("参数异常")


    def process_response(self, request, response):
        return response


class ConfusionInterceptor(MiddlewareMixin):
    """
    混淆拦截器
    """
    def process_request(self, request):
        print('混淆拦截器','process_request')
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
        print('混淆拦截器','process_response')
        if needEncrypt(request, response) and response.status_code == 200:
            #进行加密
            encrypt(response)
        return response


class ContentTypeInterceptor(MiddlewareMixin):
    """
    ContentType拦截器
    """
    def process_request(self, request):
        pass
    def process_response(self, request, response):
        response['Content-Type'] = 'application/json;charset=UTF-8'
        return response



def needLogin(request):
    """
    判断是否需要登录
    :param request:
    :return:
    """
    path = request.path
    session = request.session.get('user', None)
    if path != '/user/login/' and session == None:
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
    if path != '/user/login/' and session == None:
        return True
    else:
        return False


def needDecrypt(request):
    """
    判断是否需要解密
    :param request:
    :return:
    """
    # path = request.path
    # session = request.session.get('user', None)
    return True


def needEncrypt(request, response):
    """
    判断是否需要加密
    :param request:
    :return:
    """
    # path = request.path
    # session = request.session.get('user', None)
    return True


def encrypt(response):
    """
    加密
    :param response:
    :return:
    """
    # 缓存原始数据
    data = response.content;
    # 清空原始数据
    response.content = ''
    # 加密
    data = AES.encryptBytes(data)
    # 写入新数据
    response.write('{"ay":"')
    response.write(data)
    response.write('"}')


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
