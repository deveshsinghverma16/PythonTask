from django.urls import path

from . import views
urlpatterns = [
    path('paymentProcess',views.paymentProcess,name='paymentProcess')
]
