from django.urls import path 
from . import views

app_name = "accounts"

urlpatterns = [
	path('sign-up/', views.SignUpView.as_view(), name="sign-up"),
	path('sign-in/', views.SignInView.as_view(), name="sign-in"),
	path('sign-out/', views.sign_out, name="sign-out"),
	path('account/', views.AccountView, name="account"),
    path('account-dashboard/', views.dashboard, name="account-dashboard"),
	path('account-<int:character_id>/', views.character_details, name = "account-details")
] 

