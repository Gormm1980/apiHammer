from django.urls import path
from .views import *
app_name = 'oldhammer'
urlpatterns = [
    path('/empire', Empire_APIView.as_view()), 
    path('/empire/<int:pk>/', Empire_APIView_Detail.as_view()),
    
]