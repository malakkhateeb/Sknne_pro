from django.db import models
import re
import bcrypt
from datetime import datetime


class UserManager(models.Manager):
    def signup_validator(self , postData):
        errors = {}
        if len(postData['first_name']) < 2 : 
            errors['first_name'] = 'First Name must be at least 2 characters '
        if len(postData['last_name']) < 2 : 
            errors['last_name'] = 'Last Name must be at least 2 characters '
        if len(postData['password']) < 8 : 
            errors['password'] = 'Password should be at least 8 characters'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):      
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email = postData['email']).exists():
            errors['email'] = "Email already exists"
        if len(postData['number']) < 10 : 
            errors['number'] = 'Number should be 10 characters starting with 05*****'
        return errors
    def login_validator(self , postData):
        warnings = {}
        if postData['email'] == "":
            warnings['email'] = 'Email field cant be empty'
        elif postData['password'] == '':
            warnings['password'] = 'Password field cant be empty'
        elif User.objects.filter(email = postData['email']).exists() == False : 
                warnings['email'] = "Email does not exist"
        else:
            if bcrypt.checkpw(postData['password'].encode(), view_user(email = postData['email']).password.encode()) == False :
                warnings['password'] = 'Incorrect Email/Password'
        return warnings



class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.email


class City(models.Model):
    name = models.CharField(max_length=45)
    zip_code = models.CharField(max_length=45,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Appartment(models.Model):
    owner = models.ForeignKey(User, related_name='appartments' , on_delete=models.CASCADE)
    building_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, related_name='appartments', on_delete=models.CASCADE)
    title = models.CharField(max_length=45)
    overview = models.TextField()
    price = models.IntegerField()
    room_count = models.IntegerField()
    address = models.TextField()
    longitude = models.TextField(default="")
    latitude = models.TextField(default="")
    place_id = models.TextField(default="")
    rating = models.FloatField(default=0)
    total_votes = models.FloatField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} in {self.city.name}"

class Image(models.Model):
    appartment = models.ForeignKey(Appartment , related_name='images' , on_delete=models.CASCADE)
    images = models.FileField(upload_to='static/appartments/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Estimation(models.Model):
    user = models.ForeignKey(User,related_name='estimation', on_delete=models.CASCADE)
    appartment = models.ForeignKey(Appartment,related_name='estimation' , on_delete=models.CASCADE) # Added to track votes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Rating {self.rating} for {self.appartment.title}"


def view_user(email):
    return User.objects.get(email = email)

def show_user(id):
    return User.objects.get(id = id)

def create_user(first_name , last_name , email , password , phone_number):
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return User.objects.create(first_name = first_name , last_name = last_name , email = email ,password = pw_hash ,  phone_number = phone_number)


def show_city(name):
    return City.objects.get(name = name)

def show_room(id):
    return Appartment.objects.get(id=id)

def room_owner(id):
    room = Appartment.objects.get(id=id)
    return room.owner.id

def check_estimation(user_id , appartment_id):
    if Estimation.objects.filter(user_id = user_id , appartment_id = appartment_id).exists() == True : 
        return True
    else:   
        return False

def estimation( user , appartment ):
    return Estimation.objects.create( user = user , appartment = appartment )

def vote(id , rating):
    room = show_room(id=id)
    room.total_votes = (float(room.total_votes)+1)
    room.rating = (((float(room.rating) + float(rating))/(float(room.total_votes))))
    return room.save()