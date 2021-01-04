from django.urls import path,include
from .views import HomeView,DetailedView

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('<int:pk>/', DetailedView.as_view() , name='detailed_view'),
]

