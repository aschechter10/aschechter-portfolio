from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {}
    if request.method == "GET":
        email_success = request.GET.get('email')
        if email_success != 0 and email_success != None:
            context["success_msg"] = "Email sent successfully!"
    return render(request, "main/index.html", context)

def resume(request):
    return render(request, "main/resume.html")

def projects(request):
    return render(request, "main/projects.html")

def contact(request):
    return render(request, "main/contact.html")

def contact_request(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email_or_phone = request.POST.get("email")
        message = request.POST.get("message")
        send_mail(
            subject='Someone has contacted you',
            message= name + ' has reached out to you. Info: ' + email_or_phone + '\nMessage: ' + message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['aschechter03@gmail.com', 'alschechter@wpi.edu'])
        return redirect('/?email=1')
    else:
        return HttpResponse("Something went wrong")