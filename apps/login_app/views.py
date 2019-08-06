from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import User
# Create your views here.
def index(request):
    print('the login and registration page is being displayed')
    return render(request, 'login_app/index.html')

def success(request):
    print('currently displaying the success page!')
    return render(request, 'login_app/success.html')

def add_user(request):
    print('*'*50)
    print('the add user method is running!')
    print('password: ', request.POST["password_reg"])
    print('password conf: ', request.POST["confirm_password_reg"])
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        print('*'*50, 'creating user')
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email_address=request.POST["email"], password=request.POST["password_reg"], password_conf=request.POST["confirm_password_reg"])
        new_user = User.objects.last()
        request.session['new_user_id'] = new_user.id
        request.session['name'] = new_user.first_name
        return redirect('/success')

def login(request):
    print('the login method is running')
    errors = User.objects.login_validator(request.POST)
    print('*'*50, errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user_match = User.objects.get(email_address=request.POST['email_log'], password=request.POST['password_log'])
        request.session['new_user_id'] = user_match.id
        request.session['name'] = user_match.first_name
        return redirect('/success')

def logout(request):
    print('the logout method is running')
    request.session.clear()
    return redirect('/')