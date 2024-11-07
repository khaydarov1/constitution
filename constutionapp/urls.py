from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Bosh sahifa
    path('section/<int:section_id>/', views.section_detail, name='section_detail'),
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
]
