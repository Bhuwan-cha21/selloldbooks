from email import message
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from .models import Blog
from . forms import Edit_Blog
from django.core.mail import send_mail


# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'base.html' , context)


def register(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname =  request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['email']
        pass1 =  request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 != pass2:
            messages.warning(request,"Password diddt match")
            return redirect('register')
        elif User.objects.filter(username= uname).exists():
            messages.warning(request, "Username already exists")
            return redirect('register')
        elif User.objects.filter(email= email).exists():
            messages.warning(request, "Email already exists")
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
            user.save()
            messages.success(request,'User creatd successfully')
            message = f'Hi {fname},You has been registred successfully on Knowledge gainer Blogs.'
            subject = 'about registration'
            sender = 'wonlytech@gmail.com'
            receiver = [email,]
            send_mail(subject, message , sender , receiver)

            return redirect('login_user')
    else:
        return render(request, 'register.html')




def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfully')
            return redirect('/')
            
        else:
            messages.warning(request,'Credential Error')
            return redirect('login_user')

    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('/')
def post_blog(request):

    
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        blog = Blog(title=title,dsc=desc,user_id=request.user) 
        blog.save()
        messages.success(request, "Blog posted successfully")
        return redirect('/')
    else:
        return render(request , 'blog_post.html')
def blog_detail(request,id):
    print(id)
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_detail.html' , {'blog':blog})
def blog_delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('/')
def blog_edit(request,id):
    blog = Blog.objects.get(id=id)
    editblog = Edit_Blog(instance=blog)
    if request.method=='POST':
        form = Edit_Blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,'POST has been updated')
            return redirect('/')
    return render(request,'edit_blog.html',{'edit_blog':editblog})