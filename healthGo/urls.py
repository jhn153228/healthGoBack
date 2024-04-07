from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("routines", views.RoutineViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "workouts/",
        views.WorkOutListAPIView.as_view(),
        name="workouts_list",
    ),
]
