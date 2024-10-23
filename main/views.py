from django.shortcuts import render, redirect
from .models import File
from .forms import FileForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videos')
    form = FileForm()
    return render(request, 'main/form.html', {"form":form})

def videos(request):
    videos = File.objects.all()
    return render(request, 'main/video.html', {'videos':videos})