from rest_framework import serializers
from .models import PaymentModel
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields=['id','cardNumber','cardName','secNumber','expiry','amount']
        
        