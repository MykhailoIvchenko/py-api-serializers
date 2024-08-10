from django.urls import path, include
from rest_framework import routers

app_name = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie", MovieViewSet)
router.register("movie_session", MovieSessionViewSet)

urlpatterns = [
    path("", include("cinema.urls")),
]
