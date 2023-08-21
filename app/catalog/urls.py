from rest_framework.routers import DefaultRouter

from app.catalog.views import AuthorModelViewSet
from django.urls import path, include


router = DefaultRouter(trailing_slash=False)
router.register("author-modelviewset", AuthorModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
