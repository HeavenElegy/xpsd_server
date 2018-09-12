from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


# 登录拦截器
class LoginInterceptor(MiddlewareMixin):
    def process_request(self, request):
        if needLogin(request):
            return HttpResponse("需要登录")

    def process_response(self, request, response):
        return response


# 鉴权拦截器
class AuthenticationInterceptor(MiddlewareMixin):
    def process_request(self, request):

        # 1. 判断是否需要鉴权
        # 1.1. 根据情况进行鉴权
        if needAuthentication(request):
            return HttpResponse("鉴权失败")

        # 2. 判断是否需要解密
        # 2.1. 根据情况进行解密
        if needDecrypt(request):
            pass


    def process_response(self, request, response):
        return response


# 判断是否需要登录
def needLogin(request):
    path = request.path
    session = request.session.get('user', None)
    if path != '/login/' and session == None:
        return True
    else:
        return False


# 判断是否需要鉴权
def needAuthentication(request):
    path = request.path
    session = request.session.get('user', None)
    if path != '/login/' and session == None:
        return True
    else:
        return False


# 判断是否需要解密
def needDecrypt(request):
    path = request.path
    session = request.session.get('user', None)
    if path != '/login/' and session == None:
        return True
    else:
        return False


# 解密
def decrypt(request):
    pass