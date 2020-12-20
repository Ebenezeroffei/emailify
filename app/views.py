from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from django.core.mail import EmailMessage

# Create your views here.

class SendEmailView(generic.View):
    def get(self,request,*args,**kwargs):
        to = request.GET.get('to').split(',')
        subject = request.GET.get('subject')
        message = request.GET.get('message')
        print(to)
        print(subject)
        print(message)
        email = EmailMessage(subject = subject,body = message,to = to)
        email.send()
        data = {
            'success': True,
        }
        return JsonResponse(data)

