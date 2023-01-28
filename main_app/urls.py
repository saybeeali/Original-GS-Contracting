from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('success/', views.Success.as_view(), name="success"),
    path('contact/', views.Contact, name="contact"),
    path('projects/', views.ProjectList.as_view(), name="project_list"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project_detail"),

]