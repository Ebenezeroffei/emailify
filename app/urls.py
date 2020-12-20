from django.urls import path
from . import views as app_views

app_name = 'app'
urlpatterns = [
    path('send/email/',app_views.SendEmailView.as_view(),name = 'send_email')
]
