from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from Oddam_w_dobre_ręce_App.models import Donation, Institution
from django.contrib import messages
# Create your views here.

class LandingPage(View):


    def get(self, request):
        bags = Donation.objects.count()
        supported_institutions = Institution.objects.count()
        institutions = Institution.objects.all()
        context = {
            "bags": bags,
            "supported_institutions": supported_institutions,
            "institutions": institutions,
        }
        return render(request, "index.html", context)


class AddDonation (View):
    def get(self,request):
        return render (request, "form.html")

class Login (View):
    def get(self,request):
        return render (request, "login.html")

    def post(self,request):
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main-page')
        else:
            return redirect('register')


class Register (View):
    def get(self,request):
        return render (request, "register.html")

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "The passwords are not the same")
            return redirect('register')


        if name and surname and email and password:
            user = User.objects.create_user(first_name=name, last_name=surname, email=email, password=password,
                                            username=email)
            user.save()

            messages.success(request, "You have been registered successfully!")
            return redirect('login')


@login_required
def profile(request):
    donations = Donation.objects.filter(user=request.user)
    return render(request, 'user_profile.html', {'donations': donations})