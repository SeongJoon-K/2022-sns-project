from xml.etree.ElementInclude import include
from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name="showmain"),
    path('intro/', intro, name="intro"),
    path('<int:id>', detail, name="detail"),
    path('new', new, name="new"),
    path('create', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]
