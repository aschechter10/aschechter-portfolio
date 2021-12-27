from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def resume(request):
    return render(request, "main/resume.html")

def projects(request):
    return render(request, "main/projects.html")

def contact(request):
    return render(request, "main/contact.html")
