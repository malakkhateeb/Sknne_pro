from django.shortcuts import render



def logIn(request):
    return render(request, 'index.html')
