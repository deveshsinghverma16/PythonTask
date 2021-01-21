from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from .serializers import PaymentSerializer

from .models import PaymentModel

from credit_card_checker import CreditCardChecker
import datetime
from rest_framework import status
@api_view(['GET','POST'])

def paymentProcess(request):
    if request.method=='POST':
        paymentData = JSONParser().parse(request)
        paymentSerializer = PaymentSerializer(data=paymentData)

        if paymentSerializer.is_valid():
            cardString = paymentSerializer.validated_data['cardNumber']
            date = paymentSerializer.validated_data['expiry']
            #print(valid_expiry_date(date))
            if valid_card(cardString)==True and valid_expiry_date(date)==True:

                amount = paymentSerializer.validated_data['amount']

                if amount<20:
                    cheapPaymentGateway(amount)
                elif amount>20 and amount<500:
                    expensivePaymentGateway(amount)
                elif amount>500:
                    premiumPaymentGateway(amount)


                paymentSerializer.save()
                return JsonResponse({"message":"PaymentProcessed"},status = status.HTTP_200_OK)
            else:
               return  JsonResponse({"message":"THE REQUET iS INVALID"}, status=status.HTTP_400_BAD_REQUEST)
            
            
        return JsonResponse(paymentSerializer.data,safe=False)

    elif request.method=='GET':
        payment = PaymentModel.objects.all()

        paymentSerializer = PaymentSerializer(payment,many=True)
        return JsonResponse(paymentSerializer.data,safe=False)


def valid_card(cardString):
    return CreditCardChecker(cardString).valid()

def valid_expiry_date(date):
    
    return date >  datetime.date.today()


def cheapPaymentGateway(amount):
    pass

def expensivePaymentGateway(request):
    pass

def premiumPaymentGateway(request):
    pass