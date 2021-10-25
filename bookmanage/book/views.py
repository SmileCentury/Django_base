from django.shortcuts import render, HttpResponse
from django.views import View
from django.utils.deprecation import MiddlewareMixin

class MyMiddle(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)

        self.ipList = {}


    def process_request(self,request):

        if request.path.startswith('/method'):
            client_ip = request.META['REMOTE_ADDR']
            count = self.ipList.get(client_ip,0)
            if count >=5:
                return HttpResponse('请求过多')
            self.ipList[client_ip] = count + 1
            print('该ip 已请求',count+1,'次')




class MethodView(View):

    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')

# Create your views here.
def index(request):
    return HttpResponse('ok')


def req_ar(request, a, b):
    return HttpResponse(f'<h1>a:{a}</h1></b>b:{b}')


def headers(request):
    a = request.headers.get('a')
    b = request.headers.get('b')

    return HttpResponse(f'<h1>a:{a}</h1></b>b:{b}')

from django.contrib.auth.mixins import LoginRequiredMixin
def uls(request):
    a = request.GET.get('a')
    b = request.GET.get('b')

    return HttpResponse(f'<h1>a:{a}</h1></b>b:{b}')


def json2(request):
    import json
    a = json.loads(request.body).get('a')
    b = json.loads(request.body).get('b')

    return HttpResponse(f'<h1>a:{a}</h1></b>b:{b}')


def set_cookie(request):
    res_data = HttpResponse('')
    res_data.set_cookie('a', 'itjj_cookie', max_age=60 * 60)
    return res_data


def get_cookie(request):
    res_data = HttpResponse('')
    cooki = request.COOKIES.get('a')
    res_data.content = cooki
    return res_data

def set_session(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    request.session['username'] = username
    request.session['userpassword'] = password

    return HttpResponse('set_session')

def get_session(request):
     username = request.session.get('username')
     password = request.session.get('userpassword')

     return HttpResponse(f'username:{username} password:{password}')