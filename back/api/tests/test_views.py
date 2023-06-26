""" This file contains the tests for the views. """

from django.urls import reverse
from rest_framework import status


def test_index(client):
    """This tests the index view."""
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello, world!"}
