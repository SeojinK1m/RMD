from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from backend.models import School

# Create your tests here
class SchoolTests(APITestCase):
    def test_create_and_delete_school(self):
        #create
        school = School(name = "Washington", url = "washington")
        school.save()
        getSchool = School.objects.get(url="washington")
        assert school.name == getSchool.name
        #delete
        School.objects.get(url = "washington").delete()
        assert School.objects.filter(url = "washington").count() == 0
    
