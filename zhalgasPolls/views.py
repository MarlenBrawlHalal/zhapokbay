from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Text

def index(request):
    someText = Text.objects.all()
    return render(request, 'index.html', {'someText': someText})

def change(request):
    someText = Text.objects.all()
    return render(request, 'change.html', {'someText': someText})

def update(request):
    postText = request.POST.getlist('myText')
    for i in range(len(postText)):
        text_instance = Text.objects.get(id=i+1)
        text_instance.text = postText[i]
        text_instance.save()
    return HttpResponseRedirect(reverse('index'))
