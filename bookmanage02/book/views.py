import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.
class MyMixin:

    def __init__(self, get_response=None):
        self.ip_list = {}
        self.get_response = get_response

    def __call__(self, request):
        print('请求来了')
        client_ip = request.META['REMOTE_ADDR']
        if request.path.startswith('/method'):
            client_count = self.ip_list.get(client_ip, 0)
            if client_count >= 5:
                print('你请求过多')
                return HttpResponse('你请求过多')

            self.ip_list[client_ip] = client_count + 1

        response = self.get_response(request)

        return response


class GetView(View):
    def get(self, request):
        return HttpResponse('这是get方式请求')

    def post(self, request):
        return HttpResponse('这是post请求')


def index(request):
    return render(request, 'book/index.html')


def urla(request, a, b):
    c = request.GET.get('c')
    d = request.GET.getlist('d')
    return HttpResponse(f'a:{a},b:{b},c:{c},d:{d}')


def heads(request):
    a = request.headers.get('a')
    b = request.headers.get('b')
    c = request.POST.get('c')

    da = request.body
    d = json.loads(da)['a']
    print(d)
    return HttpResponse(f'a:{a},b:{b},c:{c},d:{d}')


def resq(request):
    j = [{'a': 'itjjj', 'b': 20},
         {'c': 123, 'd': 1111}
         ]
    #
    # res = HttpResponse('1111')
    # res.status_code = 300
    # res['test1'] ='测试'
    # res.setdefault('bbb','bbbbbb')
    jd = json.dumps(j)

    return JsonResponse(j)


def set_cookies(request):
    res = HttpResponse('')
    res.set_cookie('name', 'itjj')

    return res


def get_cookie(request):
    c = request.COOKIES.get('name2')
    return HttpResponse(c)


def set_session(request):
    um = request.GET.get('username')
    pwd = request.GET.get('password')
    request.session['username'] = um
    request.session['password'] = pwd
    data = f'set_session'
    request.session.delete('username')
    return HttpResponse(data)


def get_session(request):
    pwd = request.session.get('password')

    um = request.session.get('username')
    data = f'get_session username:{um} password:{pwd}'

    return HttpResponse(data)
