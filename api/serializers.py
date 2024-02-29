# serializers.py
from rest_framework import serializers
from database.models import User, Dialogue, Messages, Organization, Customer


class OrganizationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Organization
        fields = ('id')


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField(max_length=50, required=True)
    tg_nickname = serializers.CharField(required=False, default='')
    email = serializers.CharField(required=True)
    organization_id = serializers.IntegerField(source="organization.id", allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'tg_nickname', 'organization_id']


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField(max_length=50, required=True)
    tg_nickname = serializers.CharField(required=False, default='')

    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'tg_nickname']


class OverallStatSerializer(serializers.Serializer):
    customers_amount = serializers.IntegerField()
    dialogues_amount = serializers.IntegerField()
    customer_responses_amount = serializers.IntegerField()

class UserDetailSerializer(serializers.ModelSerializer):
    overall_stat = serializers.SerializerMethodField()
    settings = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'tg_nickname', 'organization_id', 'overall_stat', 'settings']

    def get_overall_stat(self, user):
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

        return overall_stat

    def get_settings(self, user):

        settings = {

        }

        return settings