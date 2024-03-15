from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('add-book/', book_form, name='book_form'),
    path('view-book/', book_details, name='book_details'),
    path('upload-regular-form/', upload_file_regular_form, name='upload_file_regular_form'),
    path('upload-model-form/', upload_file_model_form, name='upload_file_model_form'),
    path('file-list/', file_list, name='file_list'),
]
