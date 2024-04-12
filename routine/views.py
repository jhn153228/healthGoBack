import logging

from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from routine.models import WorkOut, Routine, RoutineInfo
from routine.serializers import (
    WorkOutSerializer,
    RoutineSerializer,
    RoutineInfoSerializer,
)

logger = logging.getLogger("django")
LOG = logger.info


class RoutineViewSet(ModelViewSet):
    queryset = Routine.objects.all()
    permission_classes = [IsAuthenticated]  # 인증된 요청에 한해서 뷰 호출 허용
    serializer_class = RoutineSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(Q(user=self.request.user))
        return qs


class RoutineInfoViewSet(ModelViewSet):
    queryset = RoutineInfo.objects.all()
    permission_classes = [IsAuthenticated]  # 인증된 요청에 한해서 뷰 호출 허용
    serializer_class = RoutineInfoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(Q(routine=self.request.GET["routine_id"]))
        return qs


class WorkOutListAPIView(ListAPIView):
    queryset = WorkOut.objects.all()
    permission_classes = [AllowAny]
    serializer_class = WorkOutSerializer
