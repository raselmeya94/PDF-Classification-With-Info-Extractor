# invoice_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='index'),
    path('api/classified-pdf-info/', views.classified_pdf_information, name='classified_pdf_information'),
]
