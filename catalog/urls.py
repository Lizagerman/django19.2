from django.urls import path

from catalog.view import home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]
