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
file_path = os.path.join(models_folder, os.path.basename(pickle))
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
			name = form.cleaned_data.get('name')
			daysonmarket = form.cleaned_data.get('daysonmarket')
			engine_displacement = form.cleaned_data.get('engine_displacement')
			horsepower = form.cleaned_data.get('horsepower')
			latitude = form.cleaned_data.get('latitude')
			listing_id = form.cleaned_data.get('listing_id')
			longitude = form.cleaned_data.get('longitude')
			mileage = form.cleaned_data.get('mileage')
			savings_amount = form.cleaned_data.get('savings_amount')
			seller_rating = form.cleaned_data.get('seller_rating')
			sp_id = form.cleaned_data.get('sp_id')
			year = form.cleaned_data.get('year')
			car_specs = pd.DataFrame({"daysonmarket": daysonmarket, "engine_displacement": engine_displacement, "horsepower": horsepower, "latitude": latitude,
	       									  "listing_id": listing_id, "longitude": longitude, "mileage": mileage, "savings_amount": savings_amount, "seller_rating": seller_rating,
	       									  "sp_id": sp_id, "year": year}, index=[0]).to_numpy().reshape(1,-1)
			predictedPrice = round(int(myModel.predict(car_specs)))

			return render(request, 'prediction.html', {'name': name,
													   'predictedPrice': predictedPrice})
		else:
			return render(request, 'model.html', {'form': form})

