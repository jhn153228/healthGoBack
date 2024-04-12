from django.urls import path, include
from rest_framework.routers import DefaultRouter

from routine import views

router = DefaultRouter()
router.register("routine", views.RoutineViewSet)
router.register("routine-info", views.RoutineInfoViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "workouts/",
        views.WorkOutListAPIView.as_view(),
        name="workouts_list",
    ),
]
