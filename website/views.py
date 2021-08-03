from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

from django.http import HttpResponse

from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import scale
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import os



# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_email = request.POST['email']
		message_subject = request.POST['subject']
		message_message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['a.lozano.alonso@gmail.com'], # to email
			)
		return render(request, 'contact.html', {'message_name': message_name, 
												'message_email': message_email, 
												'message_subject': message_subject,
												'message_message': message_message})

	else:
		return render(request, 'contact.html', {})



import pickle
from django.conf import settings

models_folder = settings.BASE_DIR / 'models_folder'
file_path = os.path.join(models_folder, os.path.basename("pickle"))
myModel = pickle.load(open(file_path, "rb+"))


def model(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'model.html', {'form': form})


def signifikant(request):
	return render(request, 'signifikant.html', {})

def team(request):
	return render(request, 'team.html', {})

def project(request):
	return render(request, 'project.html', {})

def redirect(request):
	return render(request, 'model.html', {})

def prediction(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			your_name = form.cleaned_data.get('your_name')
			horsepower = form.cleaned_data.get('horsepower')
			engine_displacement = form.cleaned_data.get('engine_displacement')
			mileage = form.cleaned_data.get('mileage')
			transmission_display = form.cleaned_data.get('transmission_display')
			year = form.cleaned_data.get('year')
			fuel_tank_volume = form.cleaned_data.get('fuel_tank_volume')
			city_fuel_economy = form.cleaned_data.get('city_fuel_economy')
			highway_fuel_economy = form.cleaned_data.get('highway_fuel_economy')
			maximum_seating = form.cleaned_data.get('maximum_seating')
			car_specs = pd.DataFrame({"horsepower": horsepower, "engine_displacement": engine_displacement, "mileage": mileage, "transmission_display": transmission_display,
	       									  "year": year, "fuel_tank_volume": fuel_tank_volume, "city_fuel_economy": city_fuel_economy, "highway_fuel_economy": highway_fuel_economy, 
	       									  "maximum_seating": maximum_seating}, index=[0]).to_numpy().reshape(1,-1)
			predictedPrice = round(int(myModel.predict(car_specs)))

			return render(request, 'prediction.html', {'name': name,
													   'predictedPrice': predictedPrice})
		else:
			return render(request, 'model.html', {'form': form})

def getModel(request):
    make_name = request.POST.get('make_name')
    print(make_name)
    print('alvaro, hemos llegado aqui')
    model_name = return_model_by_make(make_name)
    return JsonResponse({'model_name': model_name})







