from django.urls import path
from . import views
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('questions/', views.question_list, name='question_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('generate-exam/', views.generate_exam, name='generate_exam'),
]