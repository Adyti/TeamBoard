from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.db import transaction
from django.db.models import Q

from .models import KBEntry, QueryLog
from .serializers import RegisterSerializer, LoginSerializer, KBEntrySerializer

class RegisterView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "username": user.username,
                    "company_name": user.company.company_name,
                    "api_key": user.company.api_key,
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

class LoginView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(
                username=username,
                password=password
            )

            if not user:
                return Response(
                    {
                        "error": "Invalid username or password"
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "access": str(refresh.access_token),
                    "company_name": user.company.company_name,
                    "api_key": user.company.api_key,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

class QueryView(APIView):

    def post(self, request):

        search_term = request.data.get("search")

        if not search_term:
            return Response(
                {
                    "error": "Search field is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        company = request.user.company

        with transaction.atomic():

            results = KBEntry.objects.filter(
                Q(question__icontains=search_term) |
                Q(answer__icontains=search_term)
            )

            QueryLog.objects.create(
                company=company,
                search_term=search_term,
                results_count=results.count()
            )

        serializer = KBEntrySerializer(results, many=True)

        return Response(
            {
                "search": search_term,
                "count": results.count(),
                "results": serializer.data,
            },
            status=status.HTTP_200_OK,
        )