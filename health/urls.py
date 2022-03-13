from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'health'
urlpatterns = [
    path('diagnos/', views.diagnos, name='diagnos'),
    path('submission-create/', csrf_exempt(views.submission_create), name='submisson_create'),
]
