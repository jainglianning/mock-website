from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin




class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 统一验证登录
        # return none 或者 不写return才会继续往下执行, 不需要执行
        if request.path == '/uauth/login/' or request.path == '/uauth/regist/':
            return None
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/uauth/login/')

        users = User.objects.filter(u_ticket=ticket)
        if not users:
            return HttpResponseRedirect('/uauth/login/')
        # 将user赋值在request请求的user上，以后可以直接判断user有没有存在
        # 备注，django自带的有user值
        request.user = users[0]