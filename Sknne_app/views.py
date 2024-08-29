from datetime import datetime
from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib import messages
from django.views import View 
from . import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Estimation, Appartment
from django.contrib.auth.models import User
import googlemaps
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from Sknne_pro.settings import EMAIL_HOST_USER


def home(request):
    if 'id' not in request.session :
        context = {
            "apartments":models.Appartment.objects.all
        }
        return render(request, 'index.html' , context)
    else:
        context = {
            'user':models.show_user(id = request.session['id']),
            "apartments":models.Appartment.objects.all
        }
        return render(request, 'index.html', context)
    

def about_us(request):
    return render (request , "about.html")


def cities(request):
    if 'id' not in request.session :
        return redirect('/')
    else:
        apartments = Appartment.objects.all()  # Get all apartments
        apartment_count = apartments.count()  # Count the number of apartments
        context = {
            'user': models.show_user(id = request.session['id']),
            'apartments': apartments,
            'apartment_count': apartment_count,
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
            request.session['name'] = user.first_name
            return redirect('/')
    else:
        return redirect('/')

def clear_email_not_registered(request):
    if 'email_not_registered' in request.session:
        del request.session['email_not_registered']
    return JsonResponse({'status': 'cleared'})






# def rate_appartment(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         appartment_id = request.POST.get('appartment_id')
#         user_rating = float(request.POST.get('rating'))

#         try:
#             user = User.objects.get(id=user_id)
#             appartment = Appartment.objects.get(id=appartment_id)

#             # Check if the user has already rated this apartment
#             try:
#                 estimation = Estimation.objects.get(user=user, appartment=appartment)
#                 # Update the existing rating
#                 total_votes = estimation.total_votes
#                 current_rating = estimation.rating
#                 rating_sum = current_rating * total_votes + user_rating
#                 total_votes += 1
#                 new_average_rating = round(rating_sum / total_votes, 2)
#                 estimation.rating = new_average_rating
#                 estimation.total_votes = total_votes
#                 estimation.save()
#                 message = f"New Average Rating: {new_average_rating} Total Votes: {total_votes}"
#             except Estimation.DoesNotExist:
#                 # Insert a new rating
#                 estimation = Estimation.objects.create(
#                     user=user,
#                     appartment=appartment,
#                     rating=user_rating,
#                     total_votes=1
#                 )
#                 message = f"Rating {user_rating} has been added for the apartment. Total Votes: 1"

#             return JsonResponse({'message': message})

#         except User.DoesNotExist:
#             return JsonResponse({'error': 'User not found'}, status=404)
#         except Appartment.DoesNotExist:
#             return JsonResponse({'error': 'Apartment not found'}, status=404)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)


# def rate_appartment(request):
#     if request.method == 'POST':
#         user = request.user
#         appartment_id = request.POST.get('appartment_id')
#         rating = int(request.POST.get('rating'))

#         appartment = Appartment.objects.get(id=appartment_id)
#         estimation, created = Estimation.objects.get_or_create(user=user, appartment=appartment)

#         estimation.rating = rating
#         estimation.save()

#         average_rating = Estimation.objects.filter(appartment=appartment).aggregate(models.Avg('rating'))['rating__avg']
#         total_votes = Estimation.objects.filter(appartment=appartment).count()

#         response_data = {
#             'average_rating': round(average_rating, 2),
#             'total_votes': total_votes
#         }
#         return JsonResponse(response_data)
#     return JsonResponse({'error': 'Invalid request'}, status=400)


def get_appartments(request):
    if request.method == "POST":
        request.session['city'] = request.POST['city']
        return redirect('/appartments')
    else: 
        return redirect('/')

def show_appartments(request):
    if 'city' not in request.session : 
        return redirect('/')
    else:
        #all_appartments = all_appartments[:2]
        context = {
            "city": models.show_city(name = request.session['city']),
            

        }
        return render(request , 'appartments.html' , context)

def get_room(request , id):
    if request.method == "POST":
        request.session['room_id'] = request.POST['room']
        return redirect('/room')
    else: 
        return redirect('/')

def show_room(request):
    if 'room_id' not in request.session : 
        return redirect('/')
    else:
        universities = models.Univirsity.objects.all()
        appartment = models.show_room(id = request.session['room_id'])
        locations = get_Locations(appartment, request)
        secondlocation = {
            'latitude':'',
            'longitude':'',
            'name':''}
        context = {
            "secondlocation":secondlocation,
            "room": appartment,
            "vote":models.check_estimation(user_id = request.session['id'] , appartment_id = request.session['room_id'] ),  
            "locations":locations[0],
            'place_id':  appartment.place_id,
            'key': settings.GOOGLE_API_KEY,
            "universities": universities,
        }
        return render(request , 'room.html' , context)
    
def get_Locations(appartment,request):
    geoCodingInformaion = GeoCodingView.getGeoCodingInfo(request)
    locations = []
    location = {
        'latitude':float(geoCodingInformaion['latitude']),
        'longitude':float(geoCodingInformaion['longitude']),
        'name':appartment.building_name
    }
    locations.append(location)
    
    return locations

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



def submit_rating(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        models.estimation( user = models.show_user(id = request.session['id']) , appartment=models.show_room(id = request.session['room_id']) )
        models.vote(id = request.session['room_id'] , rating = rating )
        return redirect('/room')
    else: 
        return redirect("/room")

#     try:
#         # Load JSON data from the request body
#         data = json.loads(request.body)
#         rating = data.get('rating')
#         room_id = request.session.get('room_id')  # Ensure room_id is stored in the session

#             # Validate and save the rating
#         if rating and room_id:
#                 # Assuming Estimation is your model
#             models.estimation(rating=rating, id=room_id , user = models.show_user(id = request.session['id'] , total_votes = 1 , appartment = models.show_room(id = request.session['room_id'])))  
#             return JsonResponse({'status': 'success', 'message': 'Rating submitted successfully'})
#     except:
#         return redirect('/')
# @csrf_exempt
# def submit_rating(request):
#     if request.method == 'POST':
#         appartment_id = request.session['room_id']
#         rating = int(request.POST.get('rating'))
#         user = request.user

#         appartment = get_object_or_404(Appartment, id=appartment_id)

#         # Check if user has already rated this apartment
#         estimation, created = Estimation.objects.get_or_create(
#             user=user,
#             appartment=models.show_room(id = request.session['room_id']),
#             defaults={'rating': rating, 'total_votes': 1}
#         )
        
#         if not created:
#             # If the user has already rated, update the rating
#             estimation.rating = rating
#             estimation.total_votes += 1  # Increment the total votes count
#             estimation.save()

#         return JsonResponse({'status': 'success'})

#     return JsonResponse({'status': 'error'}, status=400)

def logout(request):
    request.session.clear()
    return redirect('/')

class GeoCodingView(View):
    def getGeoCodingInfo(request):
        appartment = models.show_room(id = request.session['room_id'])
        if appartment.longitude and appartment.latitude and appartment.place_id != None:
            longitude = appartment.longitude
            latitude = appartment.latitude
            place_id = appartment.place_id
        else:
            city = appartment.city
            address_string = str(appartment.address) + ", " +  str(city.zip_code) + ", " + str(city.name) + ", Palestine"
            gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
            result = gmaps.geocode(address_string)[0]
            latitude = result.get('geometry', {}).get('location', {}).get('lat', None)
            longitude = result.get('geometry', {}).get('location', {}).get('lng', None)
            place_id = result.get('place_id', {})
            appartment.latitude = latitude
            appartment.longitude = longitude
            appartment.place_id = place_id
            appartment.save()

        context = {
            'longitude': longitude,
            'latitude': latitude,
            'place_id': place_id
        }
        return context


def submit_apartment(request):
    if 'id' not in request.session : 
        return redirect('/')
    else:
        if request.method == 'POST':
            user = models.show_user(id = request.session['id'])
            # file = request.FILES.get('apartment_photos[]')
            message = f" Name : {user.first_name} {user.last_name} {"\n"} Email: {user.email} {"\n"} Phone: {request.POST['contact_number']} {"\n"} City : {request.POST['city_name']} {"\n"} Building Name : {request.POST['building_name']}{"\n"} Address: {request.POST['address']}{"\n"} Number Of Rooms : {request.POST['number_of_rooms']} {"\n"} Asking Prcie : {request.POST['price']}$ {"\n"}{"\n"}"
            email1 = 'sknne.palestine@gmail.com'
            recipient_list = [email1]
            email = EmailMessage(
                "New Appartment Submission Request",
                f"{message}",
                'New Request ',
                # settings.EMAIL_HOST_USER,
                (f"{email1}",)
            )
            for file in request.FILES.getlist('apartment_photos[]'):
                email.attach(file.name, file.read(), file.content_type)
            email.send()
            # send_mail(subject , message , "New Request" , recipient_list , fail_silently=True)
            return redirect('/')
        else:
            return redirect('/')
        
def add_appartment_owner(request):
    return render (request, 'owners.html')
def show_distance(request):
    if request.method == 'POST':
        request.session['university'] = request.POST['university']
        request.session['transportation'] = request.POST['transportation']
    now = datetime.now()
    universities = models.Univirsity.objects.all()
    appartment = models.show_room(id = request.session['room_id'])
    university = models.Univirsity.objects.get(id = request.session['university'])
    city = appartment.city
    from_address_string = str(appartment.address) + ", " +  str(city.zip_code) + ", " + str(city.name) + ", Palestine"
    to_address_string = str(university.address)+ ", " + str(university.city.name) + ", Palestine"
    gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    locations = get_Locations(appartment, request)
    secondlocation = {
        'latitude': float(university.latitude),
        'longitude':float(university.longitude),
        'name': university.name
        }
    result = gmaps.distance_matrix(
        from_address_string,
        to_address_string,
        mode = request.session['transportation'],
        departure_time = now
    )
    distance = result['rows'][0]['elements'][0]['distance']['text']
    time = result['rows'][0]['elements'][0]['duration']['text']
    request.session['distance'] = distance
    request.session['time'] = time
    context = {
        "room": appartment,
        "locations":locations[0],
        "secondlocation":secondlocation,
        "universities": universities,
        'place_id':  appartment.place_id,
        'distance': distance,
        'time': time,
        'selected_transportation': request.session['transportation'],
        'selected_university': int(request.session['university']),
        'key': settings.GOOGLE_API_KEY,
    }
    return render(request , 'room.html' , context)


