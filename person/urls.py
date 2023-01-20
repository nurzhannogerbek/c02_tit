from django.urls import path

from person.views import PersonView

app_name = 'person'

urlpatterns = [
    path('persons', PersonView.as_view(), name="person-list"),
    path('persons/<int:pk>', PersonView.as_view(), name="person-detail"),
]
