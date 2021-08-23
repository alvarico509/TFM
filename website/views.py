from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from .forms import VehicleForm

from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import scale
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

import pandas as pd
import numpy as np
import pickle
import json
import os

models_folder = settings.BASE_DIR / 'models_folder'
file_path = os.path.join(models_folder, os.path.basename("pickle"))
myModel = pickle.load(open(file_path, "rb+"))

json_folder = settings.BASE_DIR / 'JSON'
filepath_2 = os.path.join(json_folder, os.path.basename("web_dic.json"))

def readJson(filename):
	with open(filename, 'r') as fp:
		return json.load(fp)

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

def team(request):
	return render(request, 'team.html', {})

def project(request):
	return render(request, 'project.html', {})

def redirect(request):
	return render(request, 'model.html', {})

def eda(request):
	return render(request, 'eda.html', {})

def model(request):
	context = {}
	if request.method == 'GET':
		   form  = VehicleForm()
		   context['form'] = form
		   return render(request, 'model.html', context)
	if request.method == 'POST':
		form  = VehicleForm(request.POST)
		if form.is_valid():
			return render(request, 'model.html', context)

def getModel(request):
	make = request.POST.get('make')
	models = return_model_by_make(make)
	return JsonResponse({'models': models})

def getBodyType(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body_types = return_body_type(make, model)
	return JsonResponse({'body_types': body_types})

def getFuelType(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel_types = return_fuel_type(make, model, body)
	return JsonResponse({'fuel_types': fuel_types})

def getTransmission(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmissions = return_transmission(make, model, body, fuel)
	return JsonResponse({'transmissions': transmissions})

def getHorsepower(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepowers = return_horsepower(make, model, body, fuel, transmission)
	return JsonResponse({'horsepowers': horsepowers})

def getEngineDisplacement(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacements = return_engine_displacement(make, model, body, fuel, transmission, horsepower)
	return JsonResponse({'displacements': displacements})

def getEngineType(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engines = return_engine_type(make, model, body, fuel, transmission, horsepower, displacement)
	return JsonResponse({'engines': engines})

def getWheelSystem(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engine_type = request.POST.get('engine_type')
	wheels = return_wheel_system(make, model, body, fuel, transmission, horsepower, displacement, engine_type)
	return JsonResponse({'wheels': wheels})

def getGear(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engine_type = request.POST.get('engine_type')
	wheel_system = request.POST.get('wheel_system')
	gears = return_gear(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system)
	return JsonResponse({'gears': gears})

def getGear(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engine_type = request.POST.get('engine_type')
	wheel_system = request.POST.get('wheel_system')
	gears = return_gear(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system)
	return JsonResponse({'gears': gears})

def getYear(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engine_type = request.POST.get('engine_type')
	wheel_system = request.POST.get('wheel_system')
	transmission_display = request.POST.get('transmission_display')
	years = return_year(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display)
	return JsonResponse({'years': years})

def getFuelTankVolume(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engine_type = request.POST.get('engine_type')
	wheel_system = request.POST.get('wheel_system')
	transmission_display = request.POST.get('transmission_display')
	tanks = return_fuel_tank_volume(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display)
	return JsonResponse({'tanks': tanks})

def getCityFuelEconomy(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engine_type = request.POST.get('engine_type')
	wheel_system = request.POST.get('wheel_system')
	transmission_display = request.POST.get('transmission_display')
	cities = return_city_fuel_economy(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display)
	return JsonResponse({'cities': cities})

def getHighwayFuelEconomy(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engine_type = request.POST.get('engine_type')
	wheel_system = request.POST.get('wheel_system')
	transmission_display = request.POST.get('transmission_display')
	highways = return_highway_fuel_economy(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display)
	return JsonResponse({'highways': highways})

def getSeats(request):
	make = request.POST.get('make')
	model = request.POST.get('model')
	body = request.POST.get('body')
	fuel = request.POST.get('fuel')
	transmission = request.POST.get('transmission')
	horsepower = request.POST.get('horsepower')
	displacement = request.POST.get('displacement')
	engine_type = request.POST.get('engine_type')
	wheel_system = request.POST.get('wheel_system')
	transmission_display = request.POST.get('transmission_display')
	seats = return_seats(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display)
	return JsonResponse({'seats': seats})

def return_model_by_make(make):
	all_data = readJson(filepath_2)
	all_models = []
	for x in all_data:
		if x['make_name'] == make:
			if x['model_name'] not in all_models:
				all_models.append(x['model_name'])
	return all_models

def return_body_type(make, model):
	all_data = readJson(filepath_2)
	all_bodies = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model):
			if x['body_type'] not in all_bodies:
				all_bodies.append(x['body_type'])
	return all_bodies

def return_fuel_type(make, model, body):
	all_data = readJson(filepath_2)
	all_fuels = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body):
			if x['fuel_type'] not in all_fuels:
				all_fuels.append(x['fuel_type'])
	return all_fuels

def return_transmission(make, model, body, fuel):
	all_data = readJson(filepath_2)
	all_transmissions = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel):
			if x['transmission'] not in all_transmissions:
				all_transmissions.append(x['transmission'])
	return all_transmissions

def return_horsepower(make, model, body, fuel, transmission):
	all_data = readJson(filepath_2)
	all_horsepowers = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission):
			if x['horsepower'] not in all_horsepowers:
				all_horsepowers.append(x['horsepower'])
	return all_horsepowers

def return_engine_displacement(make, model, body, fuel, transmission, horsepower):
	all_data = readJson(filepath_2)
	all_displacements = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)):
			if x['engine_displacement'] not in all_displacements:
				all_displacements.append(x['engine_displacement'])
	return all_displacements

def return_engine_type(make, model, body, fuel, transmission, horsepower, displacement):
	all_data = readJson(filepath_2)
	all_engines = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)) and (x['engine_displacement'] == int(displacement)):
			if x['engine_type'] not in all_engines:
				all_engines.append(x['engine_type'])
	return all_engines

def return_wheel_system(make, model, body, fuel, transmission, horsepower, displacement, engine_type):
	all_data = readJson(filepath_2)
	all_wheels = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)) and (x['engine_displacement'] == int(displacement)) and (x['engine_type'] == engine_type):
			if x['wheel_system'] not in all_wheels:
				all_wheels.append(x['wheel_system'])
	return all_wheels

def return_gear(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system):
	all_data = readJson(filepath_2)
	all_gears = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)) and (x['engine_displacement'] == int(displacement)) and (x['engine_type'] == engine_type) and (x['wheel_system'] == wheel_system):
			if x['transmission_display'] not in all_gears:
				all_gears.append(x['transmission_display'])
	return all_gears

def return_year(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display):
	all_data = readJson(filepath_2)
	all_years = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)) and (x['engine_displacement'] == int(displacement)) and (x['engine_type'] == engine_type) and (x['wheel_system'] == wheel_system) and (x['transmission_display'] == int(transmission_display)):
			if x['year'] not in all_years:
				all_years.append(x['year'])
	all_years = list(map(int, all_years))
	max_year = max(all_years) + 1
	min_year = min(all_years)
	all_years = [x for x in range(min_year, max_year)]
	return all_years

def return_fuel_tank_volume(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display):
	all_data = readJson(filepath_2)
	all_tanks = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)) and (x['engine_displacement'] == int(displacement)) and (x['engine_type'] == engine_type) and (x['wheel_system'] == wheel_system) and (x['transmission_display'] == int(transmission_display)):
			if x['fuel_tank_volume'] not in all_tanks:
				all_tanks.append(x['fuel_tank_volume'])
	return all_tanks

def return_city_fuel_economy(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display):
	all_data = readJson(filepath_2)
	all_cities = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)) and (x['engine_displacement'] == int(displacement)) and (x['engine_type'] == engine_type) and (x['wheel_system'] == wheel_system) and (x['transmission_display'] == int(transmission_display)):
			if x['city_fuel_economy'] not in all_cities:
				all_cities.append(x['city_fuel_economy'])
	return all_cities

def return_highway_fuel_economy(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display):
	all_data = readJson(filepath_2)
	all_highways = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)) and (x['engine_displacement'] == int(displacement)) and (x['engine_type'] == engine_type) and (x['wheel_system'] == wheel_system) and (x['transmission_display'] == int(transmission_display)):
			if x['highway_fuel_economy'] not in all_highways:
				all_highways.append(x['highway_fuel_economy'])
	return all_highways

def return_seats(make, model, body, fuel, transmission, horsepower, displacement, engine_type, wheel_system, transmission_display):
	all_data = readJson(filepath_2)
	all_seats = []
	for x in all_data:
		if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == int(horsepower)) and (x['engine_displacement'] == int(displacement)) and (x['engine_type'] == engine_type) and (x['wheel_system'] == wheel_system) and (x['transmission_display'] == int(transmission_display)):
			if x['maximum_seating'] not in all_seats:
				all_seats.append(x['maximum_seating'])
	return all_seats

def prediction(request):
	dic = {}
	if request.method == 'POST':
		form = VehicleForm(request.POST)
		if form.is_valid():
			model = request.POST['model']
			body_type = request.POST['body_type']
			fuel_type = request.POST['fuel_type']
			transmission = request.POST['transmission']
			horsepower = request.POST['horsepower']
			engine_displacement = request.POST['displacement']
			engine_type = request.POST['engine_type']
			wheel_system = request.POST['wheel_system']
			transmission_display = request.POST['transmission_display']
			year = request.POST['year']
			fuel_tank_volume = request.POST['fuel_tank_volume']
			city_fuel_economy = request.POST['city_fuel_economy']
			highway_fuel_economy = request.POST['highway_fuel_economy']
			maximum_seating = request.POST['maximum_seating']
			make = form.cleaned_data.get('make')
			is_new = form.cleaned_data.get('is_new')
			exterior_color = form.cleaned_data.get('exterior_color')
			mileage = form.cleaned_data.get('mileage')
			myList = [make, model, body_type, fuel_type, transmission, horsepower, engine_displacement, engine_type, wheel_system, transmission_display,
					  year, fuel_tank_volume, city_fuel_economy, highway_fuel_economy, maximum_seating]

			if ("Empty" in myList) or ("" in myList):
				return render(request, 'model.html', {'form': form,
													  'message': "Error. Form incomplete. Please, fill out every field!"})
			else:
				var_dic[make] = 1
				var_dic["model_" + model] = 1
				var_dic['is_new'] = is_new
				var_dic[body_type] = 1
				var_dic[fuel_type] = 1
				var_dic[exterior_color] = 1
				var_dic[transmission] = 1
				var_dic[wheel_system] = 1
				var_dic[engine_type] = 1
				var_dic["horsepower"] = horsepower
				var_dic["engine_displacement"] = engine_displacement
				var_dic["mileage"] = mileage
				var_dic["transmission_display"] = transmission_display
				var_dic["year"] = year
				var_dic["fuel_tank_volume"] = fuel_tank_volume
				var_dic["city_fuel_economy"] = city_fuel_economy
				var_dic["highway_fuel_economy"] = highway_fuel_economy
				var_dic["maximum_seating"] = maximum_seating

				car_specs = pd.DataFrame(var_dic, index=[0]).to_numpy().reshape(1,-1)
				predictedPrice = round(int(myModel.predict(car_specs)))

				return render(request, 'prediction.html', {'predictedPrice': predictedPrice,
														   'make': make,
														   'model': model,
														   'is_new': is_new,
														   'body_type': body_type,
														   'fuel_type': fuel_type,
														   'exterior_color': exterior_color,
														   'transmission': transmission,
														   'wheel_system': wheel_system,
														   'engine_type': engine_type,
														   'horsepower': horsepower,
														   'engine_displacement': engine_displacement,
														   'mileage': mileage,
														   'transmission_display': transmission_display,
														   'year': year,
														   'fuel_tank_volume': fuel_tank_volume,
														   'city_fuel_economy': city_fuel_economy,
														   'highway_fuel_economy': highway_fuel_economy,
														   'maximum_seating': maximum_seating})

		else:
			return render(request, 'model.html', {'form': form})

col_names = ['city_fuel_economy', 'engine_displacement', 'fuel_tank_volume', 'highway_fuel_economy', 'horsepower', 'is_new', 'maximum_seating', 'mileage', 'transmission_display', 'year', 'Convertible', 'Coupe', 'Hatchback', 'Minivan', 'Pickup Truck', 'SUV / Crossover', 'Sedan', 'Van', 'Wagon', 'Boxer 4 cylinder', 'Boxer 6 cylinder', 'Electric Motor', 'Inline 2 cylinder', 'Inline 3 cylinder', 'Inline 4 cylinder', 'Inline 5 cylinder', 'Inline 6 cylinder', 'Rotary Engine', 'V10', 'V12', 'V6', 'V8', 'W12', 'W16', 'W8', 'Biodiesel', 'Compressed Natural Gas', 'Diesel', 'Electric', 'Flex Fuel Vehicle', 'Gasoline', 'Hybrid', 'Propane', 'Black', 'Blue', 'Brown', 'Gold', 'Gray', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'Silver', 'Teal', 'Unknown', 'White', 'Yellow', 'Acura', 'Alfa Romeo', 'Aston Martin', 'Audi', 'BMW', 'Bentley', 'Bugatti', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Daewoo', 'Dodge', 'Eagle', 'FIAT', 'Ferrari', 'Fisker', 'Ford', 'GMC', 'Genesis', 'Geo', 'Honda', 'Hummer', 'Hyundai', 'INFINITI', 'Isuzu', 'Jaguar', 'Jeep', 'Karma', 'Kia', 'Lamborghini', 'Land Rover', 'Lexus', 'Lincoln', 'Lotus', 'MINI', 'Maserati', 'Maybach', 'Mazda', 'McLaren', 'Mercedes-Benz', 'Mercury', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac', 'Porsche', 'RAM', 'Rolls-Royce', 'SRT', 'Saab', 'Saturn', 'Scion', 'Smart', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo', 'model_1 Series', 'model_124 Spider', 'model_1500', 'model_1M', 'model_2 Series', 'model_200', 'model_240', 'model_240SX', 'model_3 Series', 'model_3 Series Gran Turismo', 'model_300', 'model_300-Class', 'model_3000GT', 'model_300M', 'model_300ZX', 'model_350-Class', 'model_350Z', 'model_360', 'model_360 Spider', 'model_370Z', 'model_4 Series', 'model_400-Class', 'model_420-Class', 'model_430 Scuderia', 'model_456M', 'model_458 Italia', 'model_488', 'model_4C', 'model_4Runner', 'model_5 Series', 'model_5 Series Gran Turismo', 'model_500', 'model_500-Class', 'model_500L', 'model_500X', 'model_550', 'model_560-Class', 'model_57', 'model_570GT', 'model_570S', 'model_575M', 'model_599 GTB Fiorano', 'model_6 Series', 'model_6 Series Gran Turismo', 'model_600LT', 'model_612 Scaglietti', 'model_626', 'model_650S', 'model_675LT', 'model_7 Series', 'model_718 Boxster', 'model_718 Cayman', 'model_720S', 'model_740', 'model_8 Series', 'model_812 Superfast', 'model_850', 'model_86', 'model_9-2X', 'model_9-3', 'model_9-3 SportCombi', 'model_9-4X', 'model_9-5', 'model_9-5 SportCombi', 'model_9-7X', 'model_900', 'model_911', 'model_918 Spyder', 'model_928', 'model_940', 'model_944', 'model_960', 'model_968', 'model_A-Class', 'model_A3', 'model_A3 Sportback', 'model_A4', 'model_A4 Allroad', 'model_A4 Avant', 'model_A5', 'model_A5 Sportback', 'model_A6', 'model_A6 Allroad', 'model_A7', 'model_A8', 'model_A8 Hybrid Plug-In', 'model_AMG GT', 'model_ATS', 'model_ATS Coupe', 'model_ATS-V', 'model_ATS-V Coupe', 'model_Acadia', 'model_Accent', 'model_Accord', 'model_Accord Coupe', 'model_Accord Crosstour', 'model_Accord Hybrid', 'model_Accord Hybrid Plug-In ', 'model_Achieva', 'model_ActiveHybrid 3', 'model_ActiveHybrid 5', 'model_ActiveHybrid 7', 'model_Aerio', 'model_Aerostar', 'model_Alero', 'model_Allante', 'model_Allroad', 'model_Altima', 'model_Altima Coupe', 'model_Altima Hybrid', 'model_Amanti', 'model_Amigo', 'model_Armada', 'model_Arnage', 'model_Arteon', 'model_Ascender', 'model_Ascent', 'model_Aspen', 'model_Astra', 'model_Astro', 'model_Astro Cargo', 'model_Atlas', 'model_Atlas Cross Sport', 'model_Aura', 'model_Aurora', 'model_Avalanche', 'model_Avalon', 'model_Avalon Hybrid', 'model_Avenger', 'model_Aventador', 'model_Aveo', 'model_Aviator', 'model_Axiom', 'model_Azera', 'model_Aztek', 'model_Azure', 'model_B-Series', 'model_B9 Tribeca', 'model_BRZ', 'model_Baja', 'model_Beetle', 'model_Bentayga', 'model_Bentayga Hybrid', 'model_Blackwood', 'model_Blazer', 'model_Bonneville', 'model_Borrego', 'model_Boxster', 'model_Bravada', 'model_Brooklands', 'model_C-Class', 'model_C-HR', 'model_C-Max Energi', 'model_C-Max Hybrid', 'model_C/K 1500', 'model_C/V', 'model_C30', 'model_C70', 'model_CC', 'model_CL', 'model_CL-Class', 'model_CLA-Class', 'model_CLK-Class', 'model_CLS-Class', 'model_CR-V', 'model_CR-V Hybrid', 'model_CR-Z', 'model_CT Hybrid', 'model_CT4', 'model_CT5', 'model_CT6', 'model_CT6 Hybrid Plug-In ', 'model_CTS', 'model_CTS Coupe', 'model_CTS Sport Wagon', 'model_CTS-V', 'model_CTS-V Coupe', 'model_CTS-V Wagon', 'model_CX-3', 'model_CX-30', 'model_CX-5', 'model_CX-7', 'model_CX-9', 'model_Cabrio', 'model_Cabriolet', 'model_Cadenza', 'model_Caliber', 'model_California', 'model_California T', 'model_Camaro', 'model_Camry', 'model_Camry Hybrid', 'model_Camry Solara', 'model_Canyon', 'model_Capri', 'model_Caprice', 'model_Captiva Sport', 'model_Caravan', 'model_Carrera GT', 'model_Cascada', 'model_Catera', 'model_Cavalier', 'model_Cayenne', 'model_Cayenne E-Hybrid', 'model_Cayenne Hybrid', 'model_Cayman', 'model_Celica', 'model_Century', 'model_Challenger', 'model_Charger', 'model_Cherokee', 'model_Chevy Van', 'model_Cirrus', 'model_City Express', 'model_Civic', 'model_Civic Coupe', 'model_Civic Hatchback', 'model_Civic Hybrid', 'model_Civic Type R', 'model_Civic del Sol', 'model_Clarity Hybrid Plug-In ', 'model_Classic', 'model_Cobalt', 'model_Colorado', 'model_Colt', 'model_Commander', 'model_Compass', 'model_Concorde', 'model_Continental', 'model_Continental Flying Spur', 'model_Continental GT', 'model_Continental GTC', 'model_Continental R', 'model_Continental Supersports', 'model_Contour', 'model_Cooper', 'model_Cooper Clubman', 'model_Cooper Coupe', 'model_Cooper Paceman', 'model_Corniche', 'model_Corolla', 'model_Corolla Hatchback', 'model_Corolla Hybrid', 'model_Corolla iM', 'model_Corsair', 'model_Corsica', 'model_Corvette', 'model_Cougar', 'model_Countryman', 'model_Countryman Hybrid Plug-in ', 'model_Coupe', 'model_Crossfire', 'model_Crossfire SRT-6', 'model_Crosstour', 'model_Crosstrek', 'model_Crosstrek Hybrid', 'model_Crown Victoria', 'model_Cruze', 'model_Cruze Limited', 'model_Cube', 'model_Cullinan', 'model_Cutlass', 'model_Cutlass Ciera', 'model_Cutlass Supreme', 'model_DB11', 'model_DB7', 'model_DB9', 'model_DBS', 'model_DTS', 'model_Dakota', 'model_Dart', 'model_Dawn', 'model_DeVille', 'model_Defender', 'model_Diablo', 'model_Diamante', 'model_Discovery', 'model_Discovery Series II', 'model_Discovery Sport', 'model_Durango', 'model_Durango Hybrid', 'model_E-Class', 'model_E-PACE', 'model_E-Series', 'model_ECHO', 'model_ELR', 'model_ES', 'model_ES 300', 'model_ES 300h', 'model_ES 330', 'model_ES 350', 'model_ES Hybrid', 'model_EX35', 'model_EX37', 'model_Eclipse', 'model_Eclipse Cross', 'model_Eclipse Spyder', 'model_EcoSport', 'model_Edge', 'model_Eighty-Eight', 'model_Eighty-Eight Royale', 'model_Elantra', 'model_Elantra Coupe', 'model_Elantra GT', 'model_Elantra Touring', 'model_Eldorado', 'model_Electra', 'model_Element', 'model_Elise', 'model_Enclave', 'model_Encore', 'model_Encore GX', 'model_Endeavor', 'model_Entourage', 'model_Envision', 'model_Envoy', 'model_Envoy XL', 'model_Envoy XUV', 'model_Enzo', 'model_Eos', 'model_Equator', 'model_Equinox', 'model_Equus', 'model_Escalade', 'model_Escalade ESV', 'model_Escalade EXT', 'model_Escalade Hybrid', 'model_Escape', 'model_Escape Hybrid', 'model_Escape Hybrid Plug-in', 'model_Escort', 'model_Esprit', 'model_Esteem', 'model_EuroVan', 'model_Evora', 'model_Exige', 'model_Expedition', 'model_Explorer', 'model_Explorer Hybrid', 'model_Explorer Sport', 'model_Explorer Sport Trac', 'model_Express', 'model_Express Cargo', 'model_F-150', 'model_F-150 Heritage', 'model_F-150 SVT Lightning', 'model_F-PACE', 'model_F-TYPE', 'model_F12 Berlinetta', 'model_F430', 'model_F430 Spider', 'model_F8 Tributo', 'model_FF', 'model_FJ Cruiser', 'model_FR-S', 'model_FX35', 'model_FX37', 'model_FX45', 'model_FX50', 'model_Fiero', 'model_Fiesta', 'model_Firebird', 'model_Fit', 'model_Five Hundred', 'model_Fleetwood', 'model_Flex', 'model_Flying Spur', 'model_Focus', 'model_Focus RS', 'model_Focus SVT', 'model_Forenza', 'model_Forester', 'model_Forte', 'model_Forte Koup', 'model_Forte5', 'model_Fortwo', 'model_Freelander', 'model_Freestar', 'model_Freestyle', 'model_Frontier', 'model_Fusion', 'model_Fusion Energi', 'model_Fusion Hybrid', 'model_G-Class', 'model_G25', 'model_G3', 'model_G35', 'model_G37', 'model_G5', 'model_G6', 'model_G70', 'model_G8', 'model_G80', 'model_G90', 'model_GL-Class', 'model_GLA-Class', 'model_GLB-Class', 'model_GLC-Class', 'model_GLE-Class', 'model_GLK-Class', 'model_GLS-Class', 'model_GS', 'model_GS 200t', 'model_GS 300', 'model_GS 350', 'model_GS 400', 'model_GS 430', 'model_GS 460', 'model_GS F', 'model_GS Hybrid', 'model_GT', 'model_GT-R', 'model_GTC4Lusso', 'model_GTC4Lusso T', 'model_GTI', 'model_GTO', 'model_GX', 'model_GX 470', 'model_Galant', 'model_Gallardo', 'model_Genesis', 'model_Genesis Coupe', 'model_Ghibli', 'model_Ghost', 'model_Giulia', 'model_Gladiator', 'model_Golf', 'model_Golf Alltrack', 'model_Golf R', 'model_Golf SportWagen', 'model_GranSport', 'model_GranTurismo', 'model_Grand Am', 'model_Grand Caravan', 'model_Grand Cherokee', 'model_Grand Marquis', 'model_Grand Prix', 'model_Grand Vitara', 'model_Grand Voyager', 'model_Grand Wagoneer', 'model_H3', 'model_H3T', 'model_HHR', 'model_HR-V', 'model_HS 250h', 'model_Highlander', 'model_Highlander Hybrid', 'model_Hombre', 'model_Huracan', 'model_I30', 'model_I35', 'model_ILX', 'model_ILX Hybrid', 'model_ION', 'model_ION Red Line', 'model_IPL G', 'model_IS', 'model_IS 250', 'model_IS 350', 'model_Impala', 'model_Impala Limited', 'model_Imperial', 'model_Impreza', 'model_Impreza WRX', 'model_Impreza WRX STI', 'model_Insight', 'model_Integra', 'model_Intrepid', 'model_Intrigue', 'model_Ioniq Hybrid', 'model_Ioniq Hybrid Plug-In ', 'model_J30', 'model_JX35', 'model_Jetta', 'model_Jetta GLI', 'model_Jetta Hybrid', 'model_Jetta SportWagen', 'model_Jimmy', 'model_Journey', 'model_Juke', 'model_K5', 'model_K900', 'model_Karma', 'model_Kicks', 'model_Kizashi', 'model_Kona', 'model_Kona Electric', 'model_L-Series', 'model_L300', 'model_LC', 'model_LC Hybrid', 'model_LFA', 'model_LHS', 'model_LR2', 'model_LR3', 'model_LR4', 'model_LS', 'model_LS 400', 'model_LS 430', 'model_LS 460', 'model_LS 500', 'model_LS 500h', 'model_LS 600h L', 'model_LS Hybrid', 'model_LTD Crown Victoria', 'model_LX', 'model_LX 450', 'model_LX 470', 'model_LX 570', 'model_LaCrosse', 'model_Lancer', 'model_Lancer Evolution', 'model_Lancer Sportback', 'model_Land Cruiser', 'model_Lanos', 'model_Le Baron', 'model_LeSabre', 'model_Legacy', 'model_Leganza', 'model_Levante', 'model_Liberty', 'model_Lucerne', 'model_Lumina', 'model_Lumina Minivan', 'model_M-Class', 'model_M2', 'model_M3', 'model_M30', 'model_M35', 'model_M35h', 'model_M37', 'model_M4', 'model_M45', 'model_M5', 'model_M56', 'model_M6', 'model_M8', 'model_MAZDA2', 'model_MAZDA3', 'model_MAZDA5', 'model_MAZDA6', 'model_MAZDASPEED MX-5 Miata', 'model_MAZDASPEED3', 'model_MAZDASPEED6', 'model_MDX', 'model_MDX Hybrid Sport', 'model_MKC', 'model_MKS', 'model_MKT', 'model_MKX', 'model_MKZ', 'model_MKZ Hybrid', 'model_MP4-12C', 'model_MPV', 'model_MR2', 'model_MR2 Spyder', 'model_MX-5 Miata', 'model_Macan', 'model_Magnum', 'model_Malibu', 'model_Malibu Hybrid', 'model_Malibu Maxx', 'model_Marauder', 'model_Mariner', 'model_Mariner Hybrid', 'model_Mark LT', 'model_Mark VII', 'model_Mark VIII', 'model_Matrix', 'model_Maxima', 'model_Metris', 'model_Metris Cargo', 'model_Metro', 'model_Mighty Max Pickup', 'model_Milan', 'model_Milan Hybrid', 'model_Millenia', 'model_Mirage', 'model_Mirage G4', 'model_Model S', 'model_Montana', 'model_Montana SV6', 'model_Monte Carlo', 'model_Montego', 'model_Monterey', 'model_Montero', 'model_Montero Sport', 'model_Mountaineer', 'model_Mulsanne', 'model_Murano', 'model_Murano CrossCabriolet', 'model_Murano Hybrid', 'model_Murcielago', 'model_Mustang', 'model_Mustang SVT Cobra', 'model_Mustang Shelby GT350', 'model_Mustang Shelby GT500', 'model_NSX', 'model_NV200', 'model_NX', 'model_NX 200t', 'model_NX Hybrid', 'model_Nautilus', 'model_Navigator', 'model_Neon', 'model_Neon SRT-4', 'model_New Yorker', 'model_Ninety-Eight', 'model_Niro', 'model_Niro Hybrid Plug-In', 'model_Nitro', 'model_Odyssey', 'model_Optima', 'model_Optima Hybrid', 'model_Optima Hybrid Plug-In ', 'model_Outback', 'model_Outlander', 'model_Outlander Hybrid Plug-in ', 'model_Outlander Sport', 'model_Outlook', 'model_P1', 'model_PT Cruiser', 'model_Pacifica', 'model_Pacifica Hybrid', 'model_Palisade', 'model_Panamera', 'model_Panamera E-Hybrid', 'model_Panamera Hybrid', 'model_Park Avenue', 'model_Park Ward', 'model_Paseo', 'model_Passat', 'model_Passport', 'model_Pathfinder', 'model_Pathfinder Hybrid', 'model_Patriot', 'model_Phaeton', 'model_Phantom', 'model_Phantom Coupe', 'model_Phantom Drophead Coupe', 'model_Pickup', 'model_Pilot', 'model_Portofino', 'model_Prelude', 'model_Prius', 'model_Prius Plug-In', 'model_Prius Prime', 'model_Prius c', 'model_Prius v', 'model_Prizm', 'model_ProMaster', 'model_ProMaster City', 'model_Protege', 'model_Protege5', 'model_Prowler', 'model_Q3', 'model_Q40', 'model_Q45', 'model_Q5', 'model_Q5 Hybrid', 'model_Q5 Hybrid Plug-in', 'model_Q50', 'model_Q50 Hybrid', 'model_Q60', 'model_Q7', 'model_Q70', 'model_Q70 Hybrid', 'model_Q70L', 'model_Q8', 'model_QX30', 'model_QX4', 'model_QX50', 'model_QX56', 'model_QX60', 'model_QX60 Hybrid', 'model_QX70', 'model_QX80', 'model_Quattroporte', 'model_Quest', 'model_R-Class', 'model_R32', 'model_R8', 'model_RAM 1500', 'model_RAM 50 Pickup', 'model_RAM Van', 'model_RAM Wagon', 'model_RAV4', 'model_RAV4 Hybrid', 'model_RAV4 Prime', 'model_RC', 'model_RC 200t', 'model_RC 300', 'model_RC 350', 'model_RC F', 'model_RDX', 'model_RL', 'model_RLX', 'model_RLX Hybrid Sport', 'model_RS 3', 'model_RS 4', 'model_RS 5', 'model_RS 5 Sportback', 'model_RS 6', 'model_RS 7', 'model_RS Q8', 'model_RSX', 'model_RX', 'model_RX 300', 'model_RX 330', 'model_RX 350', 'model_RX 400h', 'model_RX Hybrid', 'model_RX-8', 'model_Rabbit', 'model_Raider', 'model_Rainier', 'model_Range Rover', 'model_Range Rover Evoque', 'model_Range Rover Hybrid', 'model_Range Rover Hybrid Plug-in', 'model_Range Rover Sport', 'model_Range Rover Velar', 'model_Ranger', 'model_Ranger Chassis', 'model_Rapide', 'model_Reatta', 'model_Regal', 'model_Regal Sportback', 'model_Regal TourX', 'model_Regency', 'model_Relay', 'model_Rendezvous', 'model_Renegade', 'model_Reno', 'model_Revero', 'model_Revero GT', 'model_Ridgeline', 'model_Rio', 'model_Rio5', 'model_Riviera', 'model_Roadmaster', 'model_Roadster', 'model_Rodeo', 'model_Rodeo Sport', 'model_Rogue', 'model_Rogue Hybrid', 'model_Rogue Select', 'model_Rogue Sport', 'model_Rondo', 'model_Routan', 'model_S-10', 'model_S-Class', 'model_S-Class Coupe', 'model_S-Series', 'model_S-TYPE', 'model_S-TYPE R', 'model_S2000', 'model_S3', 'model_S4', 'model_S4 Avant', 'model_S40', 'model_S5', 'model_S5 Sportback', 'model_S6', 'model_S60', 'model_S60 R', 'model_S7', 'model_S70', 'model_S8', 'model_S80', 'model_S90', 'model_SC 400', 'model_SC 430', 'model_SL-Class', 'model_SLC-Class', 'model_SLK-Class', 'model_SLR McLaren', 'model_SLS-Class', 'model_SLX', 'model_SQ5', 'model_SQ7', 'model_SQ8', 'model_SRX', 'model_SS', 'model_SSR', 'model_STS', 'model_STS-V', 'model_SVX', 'model_SX4', 'model_Sable', 'model_Safari', 'model_Safari Cargo', 'model_Santa Fe', 'model_Santa Fe Sport', 'model_Santa Fe XL', 'model_Savana', 'model_Savana Cargo', 'model_Sebring', 'model_Sedona', 'model_Seltos', 'model_Sentra', 'model_Sephia', 'model_Sequoia', 'model_Seville', 'model_Sienna', 'model_Sierra 1500', 'model_Sierra 1500 Hybrid', 'model_Sierra 1500 Limited', 'model_Sierra 1500HD', 'model_Sierra 2500HD', 'model_Sierra Classic 1500', 'model_Silhouette', 'model_Silverado 1500', 'model_Silverado 1500HD', 'model_Silverado 2500', 'model_Silverado 2500HD', 'model_Silverado Classic 1500', 'model_Silverado Classic 1500HD', 'model_Silverado Hybrid', 'model_Silverado SS', 'model_Sky', 'model_Skylark', 'model_Solstice', 'model_Sonata', 'model_Sonata Hybrid', 'model_Sonata Hybrid Plug-In ', 'model_Sonic', 'model_Sonoma', 'model_Sorento', 'model_Soul', 'model_Spark', 'model_Spectra', 'model_Sportage', 'model_Spyder', 'model_Stealth', 'model_Stelvio', 'model_Stinger', 'model_Storm', 'model_Stratus', 'model_Suburban', 'model_Sunfire', 'model_Superamerica', 'model_Supra', 'model_T100', 'model_TC', 'model_TL', 'model_TLX', 'model_TSX', 'model_TT', 'model_TT RS', 'model_TTS', 'model_Tacoma', 'model_Tahoe', 'model_Tahoe Hybrid', 'model_Talon', 'model_Taurus', 'model_Taurus X', 'model_Telluride', 'model_Terrain', 'model_Terraza', 'model_Thunderbird', 'model_Tiburon', 'model_Tiguan', 'model_Titan', 'model_Toronado', 'model_Torrent', 'model_Touareg', 'model_Touareg 2', 'model_Touareg Hybrid', 'model_Town & Country', 'model_Town Car', 'model_Tracer', 'model_Tracker', 'model_Trailblazer', 'model_Trailblazer EXT', 'model_Trans Sport', 'model_Transit Cargo', 'model_Transit Connect', 'model_Transit Crew', 'model_Transit Passenger', 'model_Traverse', 'model_Trax', 'model_Tribeca', 'model_Tribute', 'model_Tribute Hybrid', 'model_Trooper', 'model_Truck', 'model_Tucson', 'model_Tundra', 'model_UX', 'model_UX Hybrid', 'model_Uplander', 'model_Urus', 'model_V12 Vanquish', 'model_V12 Vantage', 'model_V40', 'model_V50', 'model_V60', 'model_V70', 'model_V70 R', 'model_V8', 'model_V8 Vantage', 'model_V90', 'model_VUE', 'model_Vanquish', 'model_Vantage', 'model_Veloster', 'model_Veloster N', 'model_Veloster Turbo', 'model_Venture', 'model_Venue', 'model_Venza', 'model_Veracruz', 'model_Verano', 'model_Verona', 'model_Versa', 'model_Versa Note', 'model_Veyron', 'model_Vibe', 'model_Villager', 'model_Viper', 'model_Virage', 'model_Vitara', 'model_Volt', 'model_Voyager', 'model_WRX', 'model_WRX STI', 'model_Windstar', 'model_Windstar Cargo', 'model_Wraith', 'model_Wrangler', 'model_Wrangler Unlimited', 'model_X-TYPE', 'model_X1', 'model_X2', 'model_X3', 'model_X3 M', 'model_X4', 'model_X4 M', 'model_X5', 'model_X5 M', 'model_X6', 'model_X6 M', 'model_X7', 'model_XC', 'model_XC40', 'model_XC60', 'model_XC70', 'model_XC90', 'model_XE', 'model_XF', 'model_XF Sportbrake', 'model_XG350', 'model_XJ-Series', 'model_XK-Series', 'model_XL-7', 'model_XLR', 'model_XLR-V', 'model_XT4', 'model_XT5', 'model_XT6', 'model_XTS', 'model_XV Crosstrek', 'model_XV Crosstrek Hybrid', 'model_Xterra', 'model_Yaris', 'model_Yaris iA', 'model_Yukon', 'model_Yukon Hybrid', 'model_Yukon XL', 'model_Z3', 'model_Z3 M', 'model_Z4', 'model_Z4 M', 'model_Z8', 'model_ZDX', 'model_Zephyr', 'model_i-Series', 'model_i3', 'model_i8', 'model_iA', 'model_iM', 'model_iQ', 'model_tC', 'model_xA', 'model_xB', 'model_xD', 'Automatic Transmission (A)', 'Continuously Variable Transmission (CVT)', 'Dual Clutch Transmission (DCT)', 'Manual Transmission (M)', 'All Wheel Drive (AWD)', 'Forward Wheel Drive (FWD)', 'Four Wheel Drive (4WD)', 'Rear Wheel Drive (RWD)', 'Two Wheel Drive (4X2)']

var_dic = dict.fromkeys(col_names, 0)












