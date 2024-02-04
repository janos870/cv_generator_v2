from django.urls import path
from .views import create, convert_to_pdf, preview, cv_list

urlpatterns = [
    path('create/', create, name='create'),
    path('cv_list/', cv_list, name='cv_list'),  # Corrected path for cv_list
    path('preview/<int:user_id>/', preview, name='preview'),
    path('convert_to_pdf/<int:user_id>/', convert_to_pdf, name='convert_to_pdf'),
]

