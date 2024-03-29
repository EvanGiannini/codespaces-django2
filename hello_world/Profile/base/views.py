import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View, generic
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from array import *
from . import forms, models

from flask import request

from django.http import JsonResponse
from .forms import ClassesForm
#from .models import 

# Create your views here.



class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

def home(request):
    return render(request, "home.html")

def sign(request):
    return render(request, "sign.html")

#@login_required  
def projects(request): #matches
   return render(request, "projects.html")

@login_required  
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')
         #else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
					# create a function
                
def projects(request):
    z = 2
    x = 3
    y = 82392
    sharedInterests = [["Leah",[3,2]], ["Taylor",[1,1]]]
    # create a dictionary
    context = {"si":sharedInterests }
    #context = {
     #   "data" : [1,2,3,4,5],
      #         }

    # return response
    return render(request, "projects.html", context)
        # else process dispatch as it otherwise normally would
    return render(request, "geeks.html", context)
        

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')

class UpdateClassesView(generic.CreateView):
    #form = ClassesForm #instance=models.Books.objects.first()
    template_name = 'update_classes.html'
    model = models.Books
    form_class = ClassesForm
    success_url = "profile/"

    

    #if request.is_ajax():
    #    term = request.GET.get('term')
    #    Entry = Classes.objects.all().filter(title__icontains=term)
    #    return JsonResponse(list(Entry.values()), safe=False)
    #if request.method == 'POST':
    #    form = ClassesForm(request.POST, instance= models.Entry.objects.first())
    #    if form.is_valid():
    #        form.save()
    #        return redirect('profile/')
    #return render(request, 'update_classes.html', {'form': form})
