from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def signup(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        x=User.objects.create_user(username=username,password=password)
        x.save()
        print("user created")
        return redirect('/')


    else:

        return render(request,'b.html')
        
