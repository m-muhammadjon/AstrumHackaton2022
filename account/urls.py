from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('profile/<str:username>/', views.profile, name='profile'),
    path('dr_add_rem/<int:id>/', views.doctor_add_or_remove, name='doctor_add_or_remove'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('doctors/', views.doctors, name='doctors'),
    path('', views.home_page, name='home_page'),

]
