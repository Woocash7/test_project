from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('upload', views.ExcelFileCreate.as_view(), name='excelfile-create'),
]