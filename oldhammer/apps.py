from django.apps import AppConfig
from oldhammer.models import FeaturesModels
from oldhammer.empire.models import Commanders, Heroes, EmpireBasicTroops, EmpireSpecialTroops, EmpireSingularModel 


class OldhammerConfig(AppConfig):
   
    name = 'oldhammer'
