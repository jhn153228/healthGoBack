from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


from accounts.models import User
from accounts.serializers import UserSerializer


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs) -> Response:

        res = super().post(request, *args, **kwargs)

        response = Response(
            {
                "message": "로그인 성공",
                "refresh_token": res.data.get("refresh", None),
                "access_token": res.data.get("access", None),
            },
            status=status.HTTP_200_OK,
        )

        # response.set_cookie("refresh", res.data.get("refresh", None), httponly=True)
        # response.set_cookie("access", res.data.get("access", None), httponly=True)

        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # 리프레시 토큰을 사용하여 액세스 토큰을 재발급
        response = super().post(request, *args, **kwargs)

        # 쿠키에 새로 발급된 리프레시 토큰을 설정
        if response.status_code == status.HTTP_200_OK:
            refresh_token = response.data.get("refresh", None)
            access_token = response.data.get("access", None)

            cookie_response = Response(
                {
                    "message": "Token refreshed successfully",
                    "refresh_token": refresh_token,
                    "access_token": access_token,
                }
            )
            # cookie_response.set_cookie("refresh", refresh_token, httponly=True)
            # cookie_response.set_cookie("access", access_token, httponly=True)

            return cookie_response

        return response


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        # 쿠키에서 리프레시 토큰 가져오기
        token = request.data.get("refresh", None)

        if token:
            # 토큰을 블랙리스트에 추가하여 무효화
            refresh_token = RefreshToken(token)
            refresh_token.blacklist()  # 블랙리스트에 추가

            # 쿠키 제거
            response = Response({"message": "로그아웃 성공"}, status=status.HTTP_200_OK)
            # response.delete_cookie("refresh")  # 'refresh' 쿠키 삭제
            # response.delete_cookie("access")  # 'access' 쿠키 삭제

            return response

        return Response(
            {"error": "Token not provided"}, status=status.HTTP_400_BAD_REQUEST
        )
