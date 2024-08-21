from django.shortcuts import render , redirect
from . import models
from django.contrib import messages 

def home(request):
    if 'id' not in request.session :
        return render(request, 'index.html')
    else:
        context = {
            'user':models.show_user(id = request.session['id'])
        }
        return render(request, 'city.html', context)

def cities(request):
    if 'id' not in request.session :
        return redirect('/')
    else:
        context = {
            'user':models.show_user(id = request.session['id'])
        }
        return render(request, 'city.html', context)

def front_validation(request):
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        errors = models.User.objects.signup_validator(request.POST)
        if models.User.objects.filter(email=email).exists():
            return render(request, 'index.html', {'email_exists': True})
        if len(errors) > 0:
            for k , value in errors.items():
                messages.error(request , value)
            return redirect('/')
        else:
            new_user = models.create_user(first_name = request.POST['first_name'] , last_name = request.POST['last_name'] , email = request.POST['email'] , password = request.POST['password'] , phone_number = request.POST['number'])
            request.session['id'] = new_user.id
            return redirect('/cities')
    else:
        return redirect('/')


def login(request):
    if request.method == 'POST':
        errors = models.User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for k , value in errors.items():
                messages.warning(request , value)
            return redirect('/')
        else:
            user = models.view_user(email = request.POST['email'])
            request.session['id'] = user.id
            return redirect('/cities')
    else:
        return redirect('/')    
