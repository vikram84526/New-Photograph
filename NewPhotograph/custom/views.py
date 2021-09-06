from django.shortcuts import render, HttpResponseRedirect,redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import UserDetails


def home_page(request):
    # Its display all user details like image, caption, user_id
    objects = UserDetails.objects.all()

    return render(request, "custom/home.html", {'objects':objects})



def user_logout(request):
    # this function logout the user
    logout(request)
    return redirect('login')

def user_signup(request):
    # this function use for signup the user
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, "custom/signup.html", context)

def user_login(request):
    #  this function login the user
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:


            login(request, user)

            return redirect('home')
        else:

            messages.info(request, 'Username OR Password is incorrect')


    return render(request, "custom/login.html")



