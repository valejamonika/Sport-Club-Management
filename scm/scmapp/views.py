from django.shortcuts import render
import datetime
from .models import *


def index(request):
    return render(request,'index.html')
def user(request):
    if 'u_name' in request.session:
        param={"name":request.session.get('u_name')}
        return render(request,"user_home.html",param)
    return render(request,"user.html")
def admin1(request):
    return render(request,'admin1.html')
def user_reg(request):
    return render(request,'user_reg.html')
def for_pas(request):
    return render(request,'for_pas.html')
def user_test(request):
    if request.method=='POST':
        name=request.POST.get("uname")
        email=request.POST.get("email")
        gender=request.POST.get("mygender")
        password=request.POST.get("password")
        contact=request.POST.get("contact")
        record=User(name=name,email=email,gender=gender,password=password,contact=contact)
        record.save()
        param={"msg":"You Are SuccessFully Registered...!!!!"}
        return render(request,"user.html",param)

        
def user_check(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        try:
            user=User.objects.get(name=uname)
            if user.password==password:
                request.session['u_name']=uname
                return user_home(request)
            else:
                param={"msg":"Password Goes Not Match....."}
                return render(request,"user.html",param)
        except Exception as e:
            param={"msg":"This User name does not exist...."}
            return render(request,"user.html",param)


def user_home(request):
    if "u_name" in request.session:
        uname=request.session.get("u_name")
        param={"name":uname}
        return render(request,"user_home.html",param)
    else:
        param={"status":"You Need To Loginn First...!"}
        return render(request,"user.html",param)

def user_logout(request):
    if 'u_name' in request.session:
        del request.session['u_name']
        return render(request,'user.html')
    else:
        param={'status':"You need to login"}
        return render(request,"user.html")


def show_event(request):
    if 'u_name' in request.session:
        event=Event.objects.all()
        param={"data":event}
        return render(request,"show_event.html",param)
    else:
        param={"msg":"You need to login"}
        return render(request,"user_login.html",param)

def ground_booking(request):
    if "u_name" in request.session:
        user=User.objects.get(name=request.session.get("u_name"))
        param={"date":datetime.date.today,"record":user}
        return render(request,"ground_booking.html",param)
    else:
        param={"status":"You Need to Login First"}
        return render(request,"user_reg.html")



def data_ground_booking(request):
    if request.method=="POST":
        date=request.POST.get("date")
        time=request.POST.get("time")
        try:
            book=Book_ground.objects.get(date=date)
            param={"msg":"Date Already reserved"}
            return render(request,"ground_booking.html",param)
        except Exception as e:
            user=User.objects.get(name=request.session.get("u_name"))
            book=Book_ground(uid=user.uid,name=user.name,date=date,time=time,mobile=user.contact)
            book.save()
            param={"status":"Booking Done You Are Good To Go....!!!"}
            return render(request,"userhome.html",param)
    else:
        param={"msg":"Something Went Wrong....!!!!"}
        return render(request,"ground_booking.html",param)