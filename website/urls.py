from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('model.html', views.model, name="model"),
    path('signifikant', views.signifikant, name="signifikant"),
    path('team', views.team, name="team"),
    path('project', views.project, name="project"),
    path('prediction', views.prediction, name="prediction"),
    path('redirect', views.model, name="redirect"),
    path('get-model',views.getModel, name='get-model'),
]
