from datetime import datetime, timedelta
from database import constants

from database.models import User, Dialogue, Messages
from api.serializers import *
from math import ceil

from api import serializers

from django.contrib.auth import authenticate
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class UserAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class ClientsApiDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if not user:
            # TODO: change to logging
            print(f"Failed authentication attempt for username: {email}")
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        refresh_token = str(refresh)
        access_token = str(refresh.access_token)


        organization = user.organization
        if organization:
            customers_amount = organization.customers.count()
        else:
            customers_amount = 0
        dialogues_amount = Dialogue.objects.filter(organization__owner=user).count()
        customer_responses_amount = Messages.objects.filter(sender_user_id=user).count()

        overall_stat = {
            "customers_amount": customers_amount,
            "dialogues_amount": dialogues_amount,
            "customer_responses_amount": customer_responses_amount
        }

        user_data = UserSerializer(user).data
        user_data['overall_stat'] = overall_stat
        user_data['settings'] = {}

        data = {
            'user': user_data
        }

        response = Response(data, status.HTTP_200_OK)
        response['Token'] = f'Bearer {access_token}'
        response['X-Refresh-Token'] = f'Bearer {refresh_token}'


        return response


class OrganizationCustomers(APIView):
    def get(self, request, organization_id):
        user = request.user

        try:
            page_no = int(self.request.query_params.get("page", constants.DialoguesPagination.PAGE))
            page_size = int(self.request.query_params.get("size", constants.DialoguesPagination.SIZE))
        except ValueError:
            return Response({
                'error': "Query parameters page and size must be integer type"
            }, status.HTTP_400_BAD_REQUEST)

        if not user.organization_id:
            return Response({
                'error': "Unable to get customer list. User does not belong to any organization."
            }, status.HTTP_403_FORBIDDEN)

        if user.organization_id != organization_id:
            return Response({
                'error': "Incorrect organization_id"
            }, status.HTTP_404_NOT_FOUND)

        customers_count = user.organization.customers.count()

        from_idx = page_no * page_size - page_size
        to_idx = page_no * page_size
        customers = user.organization.customers.all()[from_idx:to_idx]

        customers_response_data = []
        for customer in customers:
            customer_data = serializers.CustomerSerializer(customer).data
            dialogue = Dialogue.objects.filter(
                organization_id=organization_id,
                customer_id=customer.id
            ).first()

            customer_had_responded = False
            if dialogue:
                response_msg = Messages.objects.filter(
                    sender_type=constants.MessageSenderType.CUSTOMER,
                    dialogue_id = dialogue.id
                ).first()

                if response_msg:
                    customer_had_responded = True

            customer_data.setdefault('dialogue_id', dialogue.id)
            customer_data.setdefault('had_responded', customer_had_responded)

            customers_response_data.append(customer_data)

        data = {
            'result': customers_response_data,
            'pagination': {
                'current_page': page_no,
                'total_records': customers_count,
                'total_pages': ceil(customers_count / page_no),
                'page_size': page_size,
            }
        }

        return Response(data, status.HTTP_200_OK)
