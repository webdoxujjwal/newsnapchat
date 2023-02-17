from tkinter import Entry

from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {'posts': posts})

def about(request):
    return render(request, "about.html")

def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/')

def single_function(request, id):
    post = Post.objects.get(id=id)
    return render(request, "post.html", {'post': post})

def create(request):
    return render(request, "create.html")

def create_process(request):
    a = request.POST['title']
    b = request.POST['text']
    post = Post.objects.create(title=a, text=b)
    post.save()

    return HttpResponseRedirect('/')

def update_form(request,id):
    post = Post.objects.get(id=id)
    return render(request, "update.html", {'post': post})

def update_post(request, id):
    post = Post.objects.get(id=id)
    x = request.POST['title']
    y = request.POST['text']
    post.title = x
    post.text = y
    post.save()
    return HttpResponseRedirect('/')