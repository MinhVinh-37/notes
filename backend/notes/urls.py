from django.urls import include, path
from notes.views import NoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", NoteViewSet, basename="notes")

urlpatterns = [
    path("", include(router.urls)),
]
