from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import User
# Create your views here.
def index(request):
    print('the login and registration page is being displayed')
    if 'logged_in' not in request.session:
        request.session['logged_in'] = False
    return render(request, 'login_app/index.html')

def success(request):
    print('currently displaying the success page!')
    if request.session['logged_in'] != True:
        return redirect('/login')
    else:
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
        hashed = bcrypt.hashpw(request.POST['password_reg'].encode(), bcrypt.gensalt())
        decoded_hash = hashed.decode()
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email_address=request.POST["email"], password=decoded_hashed)
        new_user = User.objects.last()
        request.session['new_user_id'] = new_user.id
        request.session['name'] = new_user.first_name
        request.session['logged_in'] = True
        return redirect('/success')

def login(request):
    print('the login method is running')
    print('*'*50, request.POST)
    errors = User.objects.login_validator(request.POST)
    print('*'*50, errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login")
        return redirect('/login')
    else:
        print('*'*50, 'log in successful')
        user_matches = User.objects.filter(email_address=request.POST['email_log'])
        if len(user_matches) == 0:
            messages.error(request, 'Email not found, please register')
            return redirect('/login')
        else:
            if bcrypt.checkpw(request.POST['password_login'].encode(), user_matches[0].password.encode()):
                request.session['new_user_id'] = user_matches[0].id
                request.session['name'] = user_matches[0].first_name
                request.session['logged_in'] = True
                return redirect('/success')
            else:
                messages.error(request, 'Password is incorrect')
                return redirect('/login')

def logout(request):
    print('the logout method is running')
    request.session.clear()
    request.session['logged_in'] = False
    return redirect('/')