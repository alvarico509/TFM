from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('model.html', views.model, name="model"),
    path('team', views.team, name="team"),
    path('project', views.project, name="project"),
    path('prediction', views.prediction, name="prediction"),
    path('redirect', views.model, name="redirect"),
    path('get-model',views.getModel, name='get-model'),
    path('getBodyType', views.getBodyType, name='getBodyType'),
    path('getFuelType', views.getFuelType, name='getFuelType'),
    path('getTransmission', views.getTransmission, name='getTransmission'),
    path('getHorsepower', views.getHorsepower, name='getHorsepower'),
    path('getEngineDisplacement', views.getEngineDisplacement, name='getEngineDisplacement'),
    path('getEngineType', views.getEngineType, name='getEngineType'),
    path('getWheelSystem', views.getWheelSystem, name='getWheelSystem'),
    path('getGear', views.getGear, name='getGear'),
    path('getYear', views.getYear, name='getYear'),
    path('getFuelTankVolume', views.getFuelTankVolume, name='getFuelTankVolume'),
    path('getCityFuelEconomy', views.getCityFuelEconomy, name='getCityFuelEconomy'),
    path('getHighwayFuelEconomy', views.getHighwayFuelEconomy, name='getHighwayFuelEconomy'),
    path('getSeats', views.getSeats, name='getSeats'),
]
