from django.db import models
from .models import FeaturesModels
from model_utils.models import  SoftDeletableModel

# Create your models here.

class EmpireCommanders (models.Model, SoftDeletableModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False) 
    Magic_Objects = models.TextField( blank=False, null=False)
    MountAndMonsters = models.TextField( blank=False, null=False)
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class EmpireHeroes (models.Model, SoftDeletableModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False) 
    Magic_Objects = models.TextField( blank=False, null=False)
    MountAndMonsters = models.TextField( blank=False, null=False)
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class EmpireBasicTroops(models.Model, SoftDeletableModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False)  
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name
    
class EmpireSpecialTroops(models.Model, SoftDeletableModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False)  
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name

class EmpireSingularTroops(models.Model, SoftDeletableModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False)  
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name

