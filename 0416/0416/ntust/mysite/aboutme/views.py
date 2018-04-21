from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Person
# Create your views here.
def index(request):
    persons = Person.objects.all()
    return render_to_response('aboutme.html', locals())
