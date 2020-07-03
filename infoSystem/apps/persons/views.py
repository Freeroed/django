from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Person

def index(request):
    user_name = 'Django'
    user_age = 21
    persons = Person.objects.all
    return render(request, 'person/persons.html', { 'name': user_name, 'age' : user_age, 'persons' : persons })

def test(request):
    return render(request, 'person/test.html')

def create_page(request):
    return render(request, 'person/create.html')

def create(request):
    Person.objects.create(
        name = request.POST['name'],
        surmane = request.POST['surmane'],
        birthdate = request.POST['birthdate'],
        image_url = request.POST['image_url']
    )
    return HttpResponseRedirect( reverse('persons:index'))