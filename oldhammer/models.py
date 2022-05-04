from django.db import models 
from model_utils.models import  SoftDeletableModel

# Create your models here.
class FeaturesModels(SoftDeletableModel):
    movement= models.IntegerField( blank=False, null=False)
    HA = models.IntegerField( blank=False, null=False)
    HP = models.IntegerField( blank=False, null=False)
    Strength = models.IntegerField( blank=False, null=False) 
    Resistance = models.IntegerField( blank=False, null=False)
    Health = models.IntegerField( blank=False, null=False)
    Attacks = models.IntegerField( blank=False, null=False)
    leadership = models.IntegerField( blank=False, null=False)
    Equipment_Options = models.CharField( max_length=50, blank=False, null=False)
    Points = models.IntegerField( blank=False, null=False)
  
    