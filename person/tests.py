from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from person.models import Person


class PersonTestCase(APITestCase):
    def setUp(self):
        self.data = {
            "first_name": "John",
            "last_name": "Smith",
            "email": "johnsmith@gmail.com"
        }
        self.response = self.client.post(
            reverse('person:person-list'),
            self.data,
            format="json"
        )

    def test_create_person(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().first_name, 'John')

    def test_get_persons(self):
        response = self.client.get(reverse('person:person-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 1)

    def test_get_person(self):
        person = Person.objects.get()
        response = self.client.get(
            reverse('person:person-detail', kwargs={'pk': person.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.get().first_name, 'John')

    def test_update_person(self):
        person = Person.objects.get()
        new_data = {
            "first_name": "Bob",
            "last_name": "Marley",
            "email": "bobmarley@gmail.com"
        }
        response = self.client.put(
            reverse('person:person-detail', kwargs={'pk': person.id}),
            data=new_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.get().first_name, 'Bob')

    def test_delete_person(self):
        person = Person.objects.get()
        response = self.client.delete(
            reverse('person:person-detail', kwargs={'pk': person.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)


