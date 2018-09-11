# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse,redirect

def hello(request,age):
    return  HttpResponse('Hello World! %s' % age)

def  info(request,name,age):
    return HttpResponse('%s  is %s years old.' % (name,age))

def index(request):
    if request.method == 'POST':
        user = request.POST.get('xm')
    else:
        user = None
    return render(request, 'index.html', {'user': user})

def home(request):
    return render(request, 'home.html')

def login(request):
    user = request.POST.get('username')
    password = request.POST.get('password')
    if user == 'tom' and password == '123456':
        request.session['IS_LOGINED'] = True
        return redirect('protect')
    else:
        return redirect('home')

def protect(request):
    is_login = request.session.get('IS_LOGINED', False)
    if is_login:
        return render(request, 'protect.html')
    return redirect('home')

def template(request):
    user='zhangsan'
    age=22
    friends=['lisi','wangwu','bob','alice']
    info={'phone':'12345664854','email':'zs@163.com'}
    context={
        'user':user, 'age':age,'friends':friends,'info':info,
    }
    return  render(request,'template.html',context)