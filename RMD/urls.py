
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from backend import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'schools', views.SchoolsViewset)
router.register(r'eateries', views.EateryViewset)
router.register(r'reviews', views.ReviewViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('frontend.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)