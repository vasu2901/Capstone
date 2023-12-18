from django.urls import path
from . import views
urlpatterns = [
    path("", views.hello, name="home"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout, name="logout"),
    path("contactus", views.contactus, name="contactus"),
    path("aboutus", views.aboutus, name="aboutus"),
    path("predict", views.predict, name="predict"),
    path("predictweb", views.predict_web, name="predictweb")
]
