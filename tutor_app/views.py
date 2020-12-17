from django.http import HttpResponse

from django.shortcuts import render
from.models import stregister,ttregister,login,formtutor,booknow
# Create your views here.
def home(request):
    return render(request,'homepage.html')
def reg(request):
    return render(request,'register.html')
def logins(request):
    return render(request,'login.html')
def log(request):
    first=request.POST['fist']
    email=request.POST['em']
    ph=request.POST['num']
    gender=request.POST['gen']
    pass1=request.POST['ps']
    res=stregister(first=first,email=email,ph=ph,gender=gender)
    res.save()
    log=login(username=email,password=pass1, status=1)
    log.save()
    return render(request,'login.html')
def logtr(request):
    first = request.POST['fist']
    email = request.POST['em']
    ph = request.POST['num']
    gender = request.POST['gen']
    pass1 = request.POST['ps']
    res =ttregister(first=first, email=email, ph=ph, gender=gender)
    res.save()
    log = login(username=email, password=pass1, status=2)
    log.save()

    return render(request, 'login.html')
def ttr(request):
    return render(request,'tutoreg.html')
def stformlog(request):
    return render(request, 'stsecond.html')
def tt(request):
    return render(request, 'trsecond.html')
def trformlog(request):
    username = request.POST['username']
    password = request.POST['password']
    data=login.objects.get(username=username,password=password)
    if data.status==1:
        try:
            del request.session['ss']
        except KeyError:
            pass
        request.session['ss'] = data.id
        return render(request, 'stsecond.html')


    elif data.status==2:
        data=formtutor.objects.get(email=username)
        try:
            del request.session['tt']
        except KeyError:
            pass
        request.session['tt'] = data.id

        return render(request, 'trsecond.html', {'userid': username})
    elif data.status==3:

        return render(request, 'admin.html')
    else:
        return render(request, 'login.html')

def tutorview(request):
        show = formtutor.objects.all()
        return render(request, 'tutorview.html', {"s": show})
def trreg(request):
    firstname = request.POST['first']
    lastname = request.POST['last']
    dob = request.POST['DOB']
    addr = request.POST['add']
    pins = request.POST['pin']
    city = request.POST['cit']
    state = request.POST['st']
    email = request.POST['em']
    subject = request.POST['sub']
    exp = request.POST['expc']
    doj = request.POST['DOJ']
    online = request.POST['ok']
    hour = request.POST['hr']
    tutoring=request.POST['tut']
    education=request.POST['back']
    fun=request.POST['ho']
    demo=request.POST['video']
    img=request.FILES['fileup']
    tutor = formtutor(firstname=firstname, lastname=lastname, dob=dob, addr=addr, pins=pins, city=city, state=state,
                          email=email, subject=subject, exp=exp, doj=doj, online=online, hour=hour, img=img,tutoring=tutoring,
                      education=education,fun=fun,demo=demo,status=0)
    tutor.save()

    return render(request, 'trsecond.html')
def tcomp(request):
    return render(request, 'trregistration.html')


def ad(request):
    return render(request, 'admin.html')
def order(request):


    tid = request.session['tt']
    ord = booknow.objects.filter(tid=tid)
    return render(request,'order.html',{"o": ord})

def approve(request):
    app=formtutor.objects.filter(status=0)

    return render(request, 'approval.html',{"a":app})
def approved (request):
    bab=formtutor.objects.filter(status=1)
    return render (request,'approved.html',{"b":bab})
def see(request):
    tid = request.POST['tvid']
    see = formtutor.objects.filter(id=tid)
    return render(request, 'see.html',{"e": see})
def book(request):
    try:
        del request.session['tid']
    except KeyError:
        pass
    request.session['tid']=request.POST['tid']

    return render(request,'book.html')
def book1(request):
    sub = request.POST['st']
    clas = request.POST['cl']
    board = request.POST['bod']
    cit = request.POST['cy']
    tid=request.session['tid']
    sid=request.session['ss']
    dof = request.POST['do']
    day = request.POST['da']
    hrb = request.POST['hr']
    now = booknow(tid=tid,sid=sid, dof=dof, day=day, hrb=hrb,sub=sub, clas=clas, board=board, cit=cit,status=0)
    now.save()
    return render(request, 'stsecond.html')



def check(request):
    id=request.POST['userid']
    data= formtutor.objects.get(id=id)
    data.status=1
    data.save()
    app = formtutor.objects.filter(status=0)
    return render(request, 'approval.html', {"a": app})
def check1(request):
    id=request.POST['userid']
    data=booknow.objects.get(id=id)
    data.status=1
    data.save()
    ord = booknow.objects.filter(status=0)
    return render(request, 'order.html', {"o": ord})

def ordered(request):
    ca = booknow.objects.filter(status=1)
    return render(request, 'ordered.html',{"c":ca})








