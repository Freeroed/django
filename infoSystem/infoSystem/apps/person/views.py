from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def index(request):
    user_name = 'Django'
    user_age = 21
    persons = Person.objects.all
    return render(request, 'person/persons.html', { 'name': user_name, 'age' : user_age, 'persons' : persons })

def test(request):
    return render(request, 'person/test.html')