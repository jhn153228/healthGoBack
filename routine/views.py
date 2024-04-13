import logging

from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from accounts.models import User
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

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                required=True,
                description="유저 Bearer JWT",
            )
        ],
        operation_summary="유저의 루틴 리스트",
        responses={200: RoutineSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        filter_qs = Routine.objects.filter(user=request.user)
        serializer = RoutineSerializer(filter_qs, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user_id = User.objects.filter(login_id=request.user).first().id
            routine_name = serializer.validated_data.get("routine_name")

            # 필요한 작업 수행 (예: 데이터베이스에 모델 인스턴스 생성)
            instance = Routine.objects.create(
                user_id=user_id,
                routine_name=routine_name,
                created_by=request.user,
                updated_by=request.user,
            )
            # 생성된 모델 인스턴스를 시리얼라이저를 통해 응답에 포함시킴
            serialized_data = RoutineSerializer(instance).data
            # HTTP 상태 코드 201(Created)와 함께 응답 반환
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            # 유효성 검사 실패 시 에러 응답 반환
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoutineInfoViewSet(ModelViewSet):
    queryset = RoutineInfo.objects.all()
    permission_classes = [IsAuthenticated]  # 인증된 요청에 한해서 뷰 호출 허용
    serializer_class = RoutineInfoSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "routine_id",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                required=True,
                description="루틴 ID",
            )
        ],
        operation_summary="루틴 상세 운동리스트",
        responses={200: RoutineInfoSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        # GET 요청에 필요한 필수 파라미터 정의
        required_parameters = ["routine_id"]
        for param in required_parameters:
            if param not in request.query_params:
                return Response(
                    {"error": f"Missing parameter: {param}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        filter_qs = RoutineInfo.objects.filter(
            routine=request.query_params["routine_id"]
        )
        serializer = RoutineInfoSerializer(filter_qs, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        workout_id = request.data["workout"]
        if serializer.is_valid():
            # 필요한 작업 수행 (예: 데이터베이스에 모델 인스턴스 생성)
            instance = RoutineInfo.objects.create(
                routine_id=request.query_params["routine_id"],
                workout_id=workout_id,
                info_json=serializer.validated_data.get("info_json"),
            )
            # 생성된 모델 인스턴스를 시리얼라이저를 통해 응답에 포함시킴
            serialized_data = RoutineInfoSerializer(instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkOutListAPIView(ListAPIView):
    queryset = WorkOut.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = WorkOutSerializer
