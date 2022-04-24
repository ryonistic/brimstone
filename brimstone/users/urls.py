"""All the urls related to the user login logout are listed here. 
Registration related urls have been commented out because the Registration
for teachers will be dome by the sysadmin from the panel itself."""
from django.urls import path
from . import views

urlpatterns = [
        path('login/', views.login, name="login"),
        path('logout/', views.logout, name="logout"),
        # path('register/', views.RegisterView.as_view(), name="register"),
        ]
