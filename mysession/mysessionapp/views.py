from email.policy import default
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request,'index.html')

def set_cookies(request):
    set_cookie = render(request,'set-cookie.html')
    set_cookie.set_cookie('name','viral',max_age=60)
    return set_cookie

def get_cookies(request):
    cookie = request.COOKIES.get('name')
    print(cookie)
    context = {
        'cookie':cookie
    }
    return render(request,'get-cookie.html',context)

def del_cookies(request):
    del_cookie = render(request,'delete-cookie.html')
    del_cookie.delete_cookie('name')
    return del_cookie

def session_set(request):
    request.session['firstname'] = "viral"
    request.session['lastname'] = "patel"
    return render(request,'set-session.html')

def session_get(request):
    firstname = request.session.get('firstname')
    lastname = request.session.get('lastname')
    key = request.session.keys()
    context = {
        'firstname':firstname,
        'lastname':lastname,
        'keys':key
    }
    return render(request,'get-session.html',context)

def session_delete(request):
    try:
        del request.session['firstname']
        del request.session['lastname']
    except  KeyError:
        pass
    return render(request,'delete-session.html')