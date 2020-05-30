from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    user_name = 'Django'
    user_age = 21
    return render(request, 'person/persons.html', { 'name': user_name, 'age' : user_age })

def test(request):
    return render(request, 'person/test.html')