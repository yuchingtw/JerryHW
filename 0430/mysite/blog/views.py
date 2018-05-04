from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.utils import timezone

from .models import Post

# Create your views here.
def index(request):
    if request.POST:
        if ('del' in request.POST):
            id = request.POST['id']
            post = Post.objects.get(pk=id)
            post.delete()
            print("DELETE" + id)
        elif ('edit' in request.POST):
            id = request.POST['id']
            print("EDIT" + id)
            return HttpResponseRedirect("post/" + id)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog.html', {'posts': posts})

def edit_post(request, id):
    if request.POST:
        post = Post.objects.get(pk=id)
        post.author = request.POST['author']
        post.title = request.POST['title']
        post.text = request.POST['text']
        post.publish()
        post.save()
        return HttpResponseRedirect("/blog")
    else:
        return render(request ,'post.html')

def new_post(request):
    if request.POST:
        author = request.POST['author']
        title = request.POST['title']
        text = request.POST['text']
        created_date = timezone.localtime(timezone.now())
        published_date = timezone.localtime(timezone.now())
        Post.objects.create(
            author = author,
            title = title,
            text = text,
            created_date = created_date,
            published_date = published_date
        )
        return HttpResponseRedirect("/blog")
    else:
        return render(request ,'post.html')