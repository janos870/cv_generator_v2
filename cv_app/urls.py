# urls.py
from django.urls import path
from .views import create, convert_to_pdf, preview

urlpatterns = [
    path('create/', create, name='create'),
    path('preview/<int:user_id>/', preview, name='preview'),
    path('convert_to_pdf/<int:user_id>/', convert_to_pdf, name='convert_to_pdf'),
]
