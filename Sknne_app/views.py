from django.shortcuts import render , redirect
from django.contrib import messages 
from . import models
from django.http import JsonResponse
from .models import Estimation, Appartment
from django.contrib.auth.models import User


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
            createdUser = models.create_user(first_name = request.POST['first_name'] , last_name = request.POST['last_name'] , email = request.POST['email'] , password = request.POST['password'] , phone_number = request.POST['number'])
            request.session['id'] = createdUser.id
            return redirect('/cities')
    else:
        return redirect('/')


# def login(request):
#     if request.method == 'POST':
#         warnings = models.User.objects.login_validator(request.POST)
#         if len(warnings) > 0:
#             for k , value in warnings.items():
#                 messages.warning(request , value)
#             return redirect('/')
#         else:
#             user = models.view_user(email = request.POST['email'])
#             request.session['id'] = user.id
#             return redirect('/cities')
#     else:
#         return redirect('/')   

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Check if the email exists in the database
        if not models.User.objects.filter(email=email).exists():
            # Set a session variable to trigger SweetAlert for unregistered email
            request.session['email_not_registered'] = True
            return redirect('/login')

        user = models.User.objects.get(email=email)  # Safe to call get() now

        # Check if the user is already logged in
        if 'id' in request.session:
            logged_in_user = models.User.objects.get(id=request.session['id'])
            if logged_in_user.email == email:
                return render(request, 'index.html', {'already_logged_in': True})
        
        errors = models.User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for k, value in errors.items():
                messages.warning(request, value)
            return redirect('/')
        else:
            user = models.view_user(email=request.POST['email'])
            request.session['id'] = user.id
            return redirect('/cities')
    else:
        return redirect('/')

def clear_email_not_registered(request):
    if 'email_not_registered' in request.session:
        del request.session['email_not_registered']
    return JsonResponse({'status': 'cleared'})



def rate_appartment(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        appartment_id = request.POST.get('appartment_id')
        user_rating = float(request.POST.get('rating'))

        try:
            user = User.objects.get(id=user_id)
            appartment = Appartment.objects.get(id=appartment_id)

            # Check if the user has already rated this apartment
            try:
                estimation = Estimation.objects.get(user=user, appartment=appartment)
                # Update the existing rating
                total_votes = estimation.total_votes
                current_rating = estimation.rating
                rating_sum = current_rating * total_votes + user_rating
                total_votes += 1
                new_average_rating = round(rating_sum / total_votes, 2)
                estimation.rating = new_average_rating
                estimation.total_votes = total_votes
                estimation.save()
                message = f"New Average Rating: {new_average_rating} Total Votes: {total_votes}"
            except Estimation.DoesNotExist:
                # Insert a new rating
                estimation = Estimation.objects.create(
                    user=user,
                    appartment=appartment,
                    rating=user_rating,
                    total_votes=1
                )
                message = f"Rating {user_rating} has been added for the apartment. Total Votes: 1"

            return JsonResponse({'message': message})

        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Appartment.DoesNotExist:
            return JsonResponse({'error': 'Apartment not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

 


def logout(request):
    request.session.clear()
    return redirect('/')
