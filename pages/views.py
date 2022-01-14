from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
    else:
        return render(request, 'registration/signup.html')


def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Credentials Invalid")
            return redirect('login')
    else:
        return render(request, 'registration/login.html')


def logout_view(request):
    auth.logout(request)
    return redirect('index')


def counter(request):
    posts = [1, 2, 3, 4, 5, 6]
    return render(request, 'post.html', {'posts': posts})


def posts(request, id):
    return render(request, 'posts.html', {'id': id})