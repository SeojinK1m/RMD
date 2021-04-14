from backend.models import School, Eatery, Review
from backend.serializers import SchoolSerializer, EaterySerializer, ReviewSerializer
from rest_framework import viewsets

# Create your views here.
class EateryViewset(viewsets.ModelViewSet):
    queryset = Eatery.objects.all()
    serializer_class = EaterySerializer
    lookup_field = 'url'

class SchoolsViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'url'

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'