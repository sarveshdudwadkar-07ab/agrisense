from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
import requests
from decouple import config


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request, user)

            messages.success(request, "Account created successfully 🎉")

            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard_view(request):

    api_key = config('WEATHER_API_KEY')
    city = "Mumbai"

    weather_data = None

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:

            weather_data = {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "condition": data["weather"][0]["description"]
            }

    except Exception as e:
        print("Weather API error:", e)

    return render(request, 'users/dashboard.html', {"weather": weather_data})


def logout_view(request):
    logout(request)
    return redirect('home')