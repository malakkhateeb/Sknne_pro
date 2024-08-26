from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib import messages 
from . import models
from django.core.mail import send_mail
from Sknne_pro.settings import EMAIL_HOST_USER

def home(request):
    if 'id' not in request.session :
        return render(request, 'index.html')
    else:
        context = {
            'user':models.show_user(id = request.session['id']),
        }
        return render(request, 'city.html', context)

def cities(request):
    if 'id' not in request.session :
        return redirect('/')
    else:
        context = {
            'user': models.show_user(id = request.session['id'])
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
            models.create_user(first_name = request.POST['first_name'] , last_name = request.POST['last_name'] , email = request.POST['email'] , password = request.POST['password'] , phone_number = request.POST['number'])
            return redirect('/')
    else:
        return redirect('/')


def login(request):
    if request.method == 'POST':
        warnings = models.User.objects.login_validator(request.POST)
        if len(warnings) > 0:
            for k , value in warnings.items():
                messages.warning(request , value)
            return redirect('/')
        else:
            user = models.view_user(email = request.POST['email'])
            request.session['id'] = user.id
            request.session['name'] = user.first_name
            return redirect('/cities')
    else:
        return redirect('/')    


def get_appartments(request):
    if request.method == "POST":
        request.session['city'] = request.POST['city']
        return redirect('/appartments')
    else: 
        return redirect('/')

def show_appartments(request):
    if 'id' not in request.session : 
        return redirect('/')
    else:
        city = models.show_city(name = request.session['city'])
        #all_appartments = all_appartments[:2]
        context = {
            "city": models.show_city(name = request.session['city']),
        }
        return render(request , 'appartments.html' , context)

def get_room(request , id):
    if request.method == "POST":
        request.session['room_id'] = request.POST['room']
        room = models.show_room(id=id)
        return redirect('/room')
    else: 
        return redirect('/')

def show_room(request):
    if 'room_id' not in request.session : 
        return redirect('/')
    else:
        context = {
            "room": models.show_room(id = request.session['room_id']),
        }
        return render(request , 'room.html' , context)

def send_email(request):
    if 'id' not in request.session : 
        return redirect('/')
    else:
        if request.method == 'POST':
            owner_id = models.room_owner(id = request.session['room_id'])
            owner_name = models.show_user(id = owner_id).first_name
            subject = "New Message Regarding Your Appartment on Sknne"
            message = f" Dear Mr. {owner_name} You Have A new Message Regarding Your Appartment on Sknne app {"\n"} Name: {request.POST['name']} {"\n"} Email: {request.POST['email']} {"\n"} Phone: {request.POST['phone']} {"\n"} Message : {request.POST['message']} {"\n"}{"\n"}{"\n"} Please Dont Reply to this message "
            email1 = models.show_user(id = owner_id).email
            recipient_list = [email1]
            send_mail(subject , message , "Sknne App" , recipient_list , fail_silently=True)
            return redirect('/room')
        else:
            return redirect('/room')


def logout(request):
    request.session.clear()
    return redirect('/')
