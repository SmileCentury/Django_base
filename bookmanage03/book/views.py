from django.shortcuts import render, HttpResponse, redirect

from django.views import View
# Create your views here.

class SessionView(View):

    def get(self,request):
        aa = request.session.get('cc')
        bb = request.session.get('dd')

        return HttpResponse(f'get_session:cc-{aa},dd-{bb}')

    def post(self,request):
        request.session['cc'] = '啊啊啊啊啊2222'
        request.session['dd'] = '不不不不不不222'

        return HttpResponse('set_session:cc,dd')

def index(request):
    return render(request, 'book/index.html')


def goods(request, a, b):
    text = f'{a},{b}'
    return HttpResponse(text)


def finds(request):
    a = request.GET.getlist('a')
    b = request.GET.get('b')

    text = f'a={a},b={b}'
    return HttpResponse(text)


def register(request):
    a = request.POST.get('password')
    text = a
    return HttpResponse(text)


def json(request):
    data = request.body

    import json
    data = json.loads(data)
    print(data)
    # head = request.headers
    # method = request.method
    # print(method)
    return HttpResponse(data)


def res(request):
    x = [{'a': 'jj', 'b': 12}, {'c': 'sdf', 'd': 123}]
    import json
    data = json.dumps(x)
    response = HttpResponse(data)

    return redirect('/index')


def set_cookie(request):
    res = HttpResponse('set_cookie')
    res.set_cookie('name', 'itjj33')
    res.set_cookie('password', '123')

    return res


def get_cookie(request):
    name = request.COOKIES.get('name')
    pwd = request.COOKIES.get('password')

    return HttpResponse(f'name:{name} pwd:{pwd}')

def set_session(request):
    request.session['aa'] = '啊啊啊啊啊'
    request.session['bb'] = '不不不不不不'

    return HttpResponse('set_session:aa,bb')

def get_session(request):
    aa = request.session.get('aa')
    bb = request.session.get('bb')

    return HttpResponse(f'get_session:aa-{aa},bb-{bb}')


