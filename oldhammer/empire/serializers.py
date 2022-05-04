from rest_framework import serializers
from .models import EmpireCommanders, EmpireHeroes, EmpireBasicTroops, EmpireSpecialTroops, EmpireSingularTroops

class EmpireCommandersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Commanders  
        exclude = ['is_removed', 'created', 'modified']

class EmpireHeroesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Heroes  
        exclude = ['is_removed', 'created', 'modified']

class EmpireBasicTroopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpireBasicTroops  
        exclude = ['is_removed', 'created', 'modified']
        
class EmpireSpecialTroopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpireSpecialTroops  
        exclude = ['is_removed', 'created', 'modified']

class EmpireSpecialTroopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpireSpecialTroops  
        exclude = ['is_removed', 'created', 'modified']