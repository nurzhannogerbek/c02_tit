from django.urls import path, include

urlpatterns = [
    path('', include('person.urls', namespace="person"))
]
