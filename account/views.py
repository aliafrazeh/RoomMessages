from django.shortcuts import render,redirect
from django.contrib.auth import forms,authenticate,login
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth import login ,authenticate
# Create your views here.
# def register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username,password=password)
#             login(request,user)
#             return redirect('home')
#     else:
#         form = forms.UserCreationForm()
#     return render(request,"registration/register.html",{'form':form})

class RegisterView(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url= reverse_lazy('home')
	template_name = "registration/register.html"
	def form_valid(self, form):
		valid = super(RegisterView, self).form_valid(form)
		username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return valid