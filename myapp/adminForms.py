import code
import imp

from django.shortcuts import redirect, render

from myapp.views import bookings
from .models import *


def addground(request):
    if request.method=="POST":
        Grounds = request.POST["ground"]
        FutsalName = request.POST["Futsalname"]
        gname = request.POST["Gname"]
        rem = request.POST["rem"]
        price = request.POST["price"]
        date = request.POST["date"]
        time = request.POST["time"]

        g=ground(Grounds=Grounds,FutsalName=FutsalName,gname=gname,rem=rem,price=price,date=date,time=time)
        g.save()

        return redirect("addground")
    else:
        return render(request,"myapp/AddGround.html")

def AllGround(request):
    gro = ground.objects.all()
    return render(request,"myapp/allground.html",{"gro":gro})


def BookedGround(request):
    gro = Book.objects.all()
    return render(request,"myapp/bookedground.html",{"gro":gro})

def DeleteGround(request,pk):
    ground.objects.filter(id=pk).delete()
    return redirect("addground")

def deletebground(request,pk):
    Book.objects.filter(id=pk).delete()
    return redirect("bookedground")