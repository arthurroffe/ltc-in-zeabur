from django.shortcuts import render
from rest_framework.permissions import AllowAny  # for Test
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import mixins, status, viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from account import serializers, models
from account.functions import ApiRes
from django.db import transaction
# Create your views here.


class TokenView(TokenViewBase):
    # permission_classes = [AllowAny]

    @extend_schema(tags=['Auth'],
                   summary='Create token (Sign in)',
                   request=serializers.CreateToken,
                   responses={200: serializers.CreateToken,
                              401: OpenApiResponse(
                                description="{'error':{'code':'code','message':'message'}}")})
    def post(self, request, *args, **kwargs):
        self._serializer_class = 'account.serializers.CreateTokenExtend'
        return super().post(request, *args, **kwargs)

    @extend_schema(tags=['Auth'],
                   summary='Renew token',
                   request=serializers.RenewToken,
                   responses={200: serializers.RenewTokenRes,
                              401: OpenApiResponse(
                                description='RefreshToken is incorrect')})
    def put(self, request, *args, **kwargs):
        self._serializer_class = 'account.serializers.RenewToken'
        return super().post(request, *args, **kwargs)


class UserViews(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        username: str = request.data.get('username')
        email: str = request.data.get('email')
        password: str = request.data.get('password')

        try:
            with transaction.atomic():
                register_user = User.objects.create_user(
                    username=username, email=email, password=password)

                user_info = {
                    "id": register_user.id
                }

            return ApiRes().set_success_msg().generate(
                status_code=200, return_data=user_info)
        except Exception as e:
            response = {
                "error": {
                    "code": 4003,
                    "message": f"Error is: {e}:{e.__class__.__name__}"
                }
            }
            return Response(status=400, data=response)

