from django.shortcuts import render
from book.models import book
from book.models import student
from book.forms import bookform
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home1.html')

def about(request):
    return render(request,"about.html")

def add(request):
    if (request.method=="POST"):
        t=request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        f=request.FILES['f']
        c=request.FILES['i']
        b=book.objects.create(title=t,author=a,price=p,pdf=f,cover=c)
        b.save()
        return home(request)
    return render(request,'addbook.html')



def add1(request):
    f=bookform()  #creating empty form object
    if (request.method == "POST"):
        print(request.POST)

        f = bookform(request.POST,request.FILES)

        if(f.is_valid()):  #createing form object using values recieved from form
            f.save()
            return home(request)
    return render(request,'add1.html',{'form':f})



def view1(request):
    b=book.objects.all()
    return render(request,"view1.html",{'book':b})
def viewbook(request,p):
    b=book.objects.get(id=p)
    return render(request,'viewbook.html',{'book':b})
def deletebook(request,p):
    b=book.objects.get(id=p)
    b.delete()
    return view1(request)
def updatebook(request,p):
    b = book.objects.get(id=p)
    f=bookform(instance=b)
    if(request.method=="POST"):
        f=bookform(request.POST,request.FILES,instance=b)
        if (f.is_valid()):  # createing form object using values recieved from form
            f.save()
            return view1(request)
    return render(request,'add1.html',{'form':f})




def students(request):
    s=student.objects.all()
    return render(request,'student.html',{'stu':s})


def addstudent(request):
    if (request.method=="POST"):
        f=request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        c = request.POST['c']
        b=student.objects.create(first_name=f,last_name=l,age=e,place=c)
        b.save()
        return students(request)
    return render(request,'addstudent.html')

def fact(request):
    if(request.method=="POST"):
        n=int(request.POST['n'])
        f=1
        for i in range(1,n+1):
            f=f*i
        return render(request,'factorial.html',{'fact':f})
    return render(request,"factorial.html")


def operation(request):
    if (request.method=="POST"):
        fn=int(request.POST['fn'])
        sn =int(request.POST['sn'])
        a =(fn+sn)
        s = (fn-sn)
        m = (fn*sn)
        d = (fn/sn)
        return render(request, 'results.html', {'sum':a,'diffrence':s,'product':m,'quotient':d})
    return render(request, "operations.html")

def search(request):
    if (request.method=="POST"):
        s=request.POST['srh']
        match=book.objects.filter(Q(title__icontains=s)| Q(author__icontains=s))
        if match:
            return render(request,'search.html',{'m':match})
        else:
            messages.error(request,"No results found")

    #return render(request,'search.html')
def register(request):
    if (request.method=='POST'):
        u = request.POST['u']
        f= request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        c = request.POST['c']
        if p==c:
            user=User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
            user.save()
            return home(request)


    return render(request,'register.html')
def user_login(request):
    if(request.method=='POST'):
        u= request.POST['u']
        p= request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,"invalid credentials")

    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return home(request)