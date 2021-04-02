from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from job.models import Job
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from job.forms import JobForm
def home(request):
    data=Job.objects.all()
    context={
        'job':data
    }
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
def list(request):
    data = Job.objects.all()[::-1]
    context = {
        'job': data
    }
    return render(request,'list.html',context)
def contactus(request):
    return render(request,'contactus.html')
def signin(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        u = request.POST['username']
        p = request.POST['pass1']
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Password mismatch")
            return redirect('signin')
def signup(request):
    if request.method=='GET':
         return render(request,'signup.html')
    else:
        u = request.POST['username']
        e = request.POST['email']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']
        if p1==p2:
            try:
                u = User(username=u, email=e)
                u.set_password(p1)
                u.save()
            except:
                messages.add_message(request, messages.ERROR, "Account Alredy Exists!!!")
                return redirect('signin')
            messages.add_message(request, messages.SUCCESS, "Signup Success!!!")
            return redirect('signin')
        else:
            messages.add_message(request,messages.ERROR,"Password Mismatch!!!")
            return redirect('signup')
@login_required(login_url='signin')
def dashboard(request):
    data=Job.objects.all()[::-1]
    context={
        'job':data
    }
    return render(request,'dashboard.html',context)
def signout(request):
    logout(request)
    return redirect('signin')
def create_post(request):
    form = JobForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context={
        'form':form
    }
    return render(request,'create_post.html',context)
def editpost(request,id):
    data=Job.objects.get(pk=id)
    form=JobForm(request.POST or None,request.FILES or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'edit_post.html', context)
def deletepost(request,id):
    b=Job.objects.get(pk=id)
    b.delete()
    return redirect('dashboard')