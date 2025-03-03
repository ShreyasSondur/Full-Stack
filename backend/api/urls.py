from django.urls import path , include
from . import views

urlpatterns = [
    path('faculty/', views.FacultyListCreate.as_view()),
    path('department/', views.DeparthmentListCreate.as_view()),
]