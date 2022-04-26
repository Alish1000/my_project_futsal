from django.urls import path
from . import views
from . import adminForms

urlpatterns = [
    path('', views.home, name="home"),
    path('findground', views.findground, name="findground"),




    path('addground', adminForms.addground, name="addground"),
    path('allground', adminForms.AllGround, name="allground"),
    path('bookedground', adminForms.BookedGround, name="bookedground"),
    path('deleteground/<int:pk>', adminForms.DeleteGround, name="deleteground"),
    path('deletebground/<int:pk>', adminForms.deletebground, name="deletebground"),
    





    path('bookings', views.bookings, name="bookings"),
    path('signup/', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('success', views.success, name="success"),
    path('signout', views.signout, name="signout"),

]
