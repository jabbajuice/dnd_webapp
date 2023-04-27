from django.urls import path 
from . import views 

app_name = "characters"

urlpatterns = [
	path('createcharacter/', views.CharacterView, name="create characters"),
]