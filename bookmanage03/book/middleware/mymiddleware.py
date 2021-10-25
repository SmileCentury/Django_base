from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class MyMiddleWare(MiddlewareMixin):
    ipList = {}
    """记录ip访问次数,实现每个IP向 /pw 开头的地址 最多请求5次"""

    def process_request(self, request):
        client_ip = request.META['REMOTE_ADDR']
        if request.path.startswith('/pw'):
            client_count = self.ipList.get(client_ip, 0)
            if client_count >= 5:
                print('超出请求限时，请稍后再试')
                return HttpResponse('超出请求限时，请稍后再试')
            self.ipList[client_ip] = client_count + 1

        print('请求来了 ip', client_ip, '请求路径', request.path, '次数', self.ipList[client_ip])

