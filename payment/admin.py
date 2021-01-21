from django.contrib import admin

# Register your models here.
from .models import PaymentModel

admin.site.register(PaymentModel)