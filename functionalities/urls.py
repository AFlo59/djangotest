from django.urls import path
from functionalities import views

urlpatterns = [
    path('', views.FunctionalitiesListView.as_view(), name="funct_list"),
    path('<int:pk>/', views.FunctionalitiesDetailView.as_view(), name='funct_detail'),
    path('signup/', views.SignupView.as_view(), name='signup')
]