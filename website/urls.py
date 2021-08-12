
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('model.html', views.model, name="model"),
    path('team.html', views.team, name="team"),
    path('project.html', views.project, name="project"),
    path('prediction.html', views.prediction, name="prediction"),
    path('redirect', views.model, name="redirect"),
    path('get-model',views.getModel, name='get-model')
]