from django.db.models import Q
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from healthGo.models import Routine, WorkOuts
from healthGo.serializers import RoutineSerializer, WorkOutSerializer
import logging
from accounts.models import User

logger = logging.getLogger("django")
LOG = logger.info


def strp_date(value):
    return_value = datetime.strptime(value, "%Y-%m-%d")
    return return_value


class RoutineViewSet(ModelViewSet):
    queryset = Routine.objects.all()  # .select_related("author")
    permission_classes = [IsAuthenticated]  # 인증된 요청에 한해서 뷰 호출 허용
    serializer_class = RoutineSerializer

    def get_queryset(self):
        req_data = self.request.GET
        qs = super().get_queryset()
        qs = qs.filter(
            Q(author=self.request.user)
        )  # FIXME: accounts 기능 추가하면 user사용하게 변경
        # work_date = datetime.today().strftime("%Y-%m-%d")
        if req_data.get("work_date"):
            work_date = strp_date(req_data.get("work_date"))
            qs = qs.filter(Q(work_date=work_date))

        return qs

    def create(self, request, *args, **kwargs):

        admin_user = User.objects.filter(username=self.request.user).first()

        routine = []
        if "form_data" in request.data:

            for work_name, set_infos in request.data["form_data"].items():
                routine.append({"work_name": work_name, "set_infos": set_infos})

            works_json = {"routine": routine}

            del request.data["form_data"]
            request.data["works_json"] = str(works_json).replace("'", '"')

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # POST 메서드에서 사용할 필드
            work_date = serializer.validated_data.get("work_date")
            # request.data["works_json"] = "" 와 같이 데이터를 임의로 조작할 땐 Validate대상에서 벗어난다.
            works_json = request.data["works_json"]
            author_id = admin_user.id

            # 필요한 작업 수행 (예: 데이터베이스에 모델 인스턴스 생성)
            instance = Routine.objects.create(
                work_date=work_date, works_json=works_json, author_id=author_id
            )

            # 생성된 모델 인스턴스를 시리얼라이저를 통해 응답에 포함시킴
            serialized_data = RoutineSerializer(instance).data

            # HTTP 상태 코드 201(Created)와 함께 응답 반환
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            # 유효성 검사 실패 시 에러 응답 반환
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        # request.data를 수정하여 저장하는 로직 추가
        routine = []
        if "form_data" in request.data:

            for work_name, set_infos in request.data["form_data"].items():
                routine.append({"work_name": work_name, "set_infos": set_infos})

            works_json = {"routine": routine}

            del request.data["form_data"]
            request.data["works_json"] = str(works_json).replace("'", '"')

        return super().update(request, *args, **kwargs)


class WorkOutListAPIView(ListAPIView):
    queryset = WorkOuts.objects.all()
    permission_classes = [AllowAny]
    serializer_class = WorkOutSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
