from django.db import models


# Create your models here.
class DeliveryModel(models.Model):
    hours = models.FloatField(default=0)
    completed_deliveries = models.IntegerField(default=0)
    delivery_price = models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    collected_money = models.FloatField(default=0)
    tips_on_card = models.FloatField(default=0)
    tips_cash = models.FloatField(default=0)
    company_fixed_commission = models.FloatField(default=0)
    company_percentage_commission = models.FloatField(default=0)
    driven_distance = models.FloatField(default=0)
    fuel_consumption_100km = models.FloatField(default=0)
    fuel_type = models.FloatField(default=0)
    fuel_price = models.FloatField(default=0)

