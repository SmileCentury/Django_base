from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('ok')


def req_ar(request, a, b):
    return HttpResponse(f'<h1>a:{a}</h1></b>b:{b}')


def headers(request):
    a = request.headers.get('a')
    b = request.headers.get('b')

    return HttpResponse(f'<h1>a:{a}</h1></b>b:{b}')


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