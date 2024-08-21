from django.shortcuts import render , redirect
from . import models
from django.contrib import messages 

def logIn(request):
    if 'id' not in request.session :
        return render(request, 'index.html')
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
            return redirect('/city')
    else:
        return redirect('/')


def login(request):
    if request.method == 'POST':
        warnings = models.User.objects.login_validator(request.POST)
        if len(warnings) > 0:
            for k, value in warnings.items():
                messages.warning(request, value)
            return redirect('/')
        else:
            try:
                user = models.view_user(email=request.POST['email'])
                request.session['id'] = user.id
                return redirect('/city')
            except models.User.DoesNotExist:
                messages.error(request, "Invalid login credentials")
                return redirect('/')
    else:
        return redirect('/')    


    
    
def city(request):
    if 'id' in request.session:
        user = models.show_user(request.session['id'])
        context = {'user': user}
        return render(request, 'city.html', context)
    else:
        return redirect('/')
