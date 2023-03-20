from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerRegisterForm, DeveloperRegisterForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.conf import settings
#send mail
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegisterForm
    template_name = 'user/manager_register.html'
    success_url = "/"

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'manager'
    #     return super().get_context_data(**kwargs)

    def form_valid(self,form):
        email = form.cleaned_data.get('email')
        mail_response = sendMail(email)
        # print(mail_response)
        if mail_response > 0:
            user = form.save()
            login(self.request,user)
            return super().form_valid(form)
            # return HttpResponse('Mail Sent')
        else:
            print('Failed to send mail')
            # return HttpResponse('Failed to send mail')
    
class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegisterForm
    template_name = 'user/developer_register.html'
    success_url = "/"

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'developer'
    #     return super().get_context_data(**kwargs)

    def form_valid(self,form):
        email = form.cleaned_data.get('email')
        mail_response = sendMail(email)
        # print(mail_response)
        if mail_response > 0:
            user = form.save()
            login(self.request,user)
            return super().form_valid(form)
            # return HttpResponse('Mail Sent')
        else:
            print('Failed to send mail')
            # return HttpResponse('Failed to send mail')

class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager1:
                return '/cbv/list/'
            elif self.request.user.is_devleopr:
                return '/developer/'
            else:
                return '/no_role/'
            

# def sendMail(request):
#     subject = "welcome to django"
#     message = "hello django"
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['tirthop812002@gmail.com']
#     res = send_mail(subject,message,email_from,recipient_list)
#     if res>0:
#         print("mail sent")
#     else:
#         print("mail not sent")    
#     print(res)
#     return HttpResponse("mail sent")

def sendMail(email):
    subject = 'Welcome to the PG Finder'
    message = 'We are glad to welcome you. Our Website helps you to find out best PG according to your requirements'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    mail_response = send_mail(subject,message,email_from,recipient_list)
    return mail_response