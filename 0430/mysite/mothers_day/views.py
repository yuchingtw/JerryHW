from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .models import Message

# Create your views here.

def index(request):
    message = Message.objects.all()
    return render(request, 'mothers_day.html', {'message':message})

def post_message(request):
    request.encoding='utf-8'
    name = request.POST['name']
    title = request.POST['title']
    content = request.POST['content']
    date_time = timezone.localtime(timezone.now())
    Message.objects.create(
        name = name,
        title = title,
        content = content,
        date_time = date_time
    )
    return HttpResponseRedirect(".")