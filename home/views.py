from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages
from .models import Wiki



# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        # check if user has entered correct credentials
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request, 'login.html')    
    

def logoutUser(request):
    logout(request)
    # Redirect to a success page.
    return redirect("/login")


def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # checks for erraneous input

        # Create the user

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request," Your account has been successfully created")
        return redirect("/")
        # messages.success(request," Your account has been successfully created")

    return render(request,'register.html')
    # else:
    #     return HttpResponse('404 - Not Found')

    
    

def search(request):
    query=request.GET.get('search')
    if len(query)<2 :
        info = []
    else:

        info=Wiki.objects.distinct().filter(unique_source__contains=query)
    return render(request,'search.html',{'info':info})
    # return HttpResponse(qur)

def evalpage(request, user):
    x=Wiki.objects.filter(correct=1, source=user)
    y=Wiki.objects.filter(correct=0, source=user)
    return render(request,'second_search.html',{'x':x,'y':y})


