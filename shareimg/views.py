from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from models import SharedImage

def index(request):
    images = SharedImage.objects.all()
    return render(request, 'index.html', {'images':images})
        
def handle_upload(request):
    new_img = SharedImage()
    new_img.image = request.FILES['file']
    new_img.title = request.POST['title']
    new_img.description = request.POST['description']
    new_img.save()
    return HttpResponseRedirect('/')
    
