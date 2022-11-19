from rest_framework import serializers
from .models import Aprea_memberships, user,artical,Publications,media, license_Person, license_Company,artical_comments


class us(serializers.ModelSerializer):
    class Meta:
        model=user
        fields="__all__"


class As(serializers.ModelSerializer):
    class Meta:
        model=artical
        fields="__all__"


class P_S(serializers.ModelSerializer):
    class Meta:
        model=Publications
        fields='__all__'

class media_ser(serializers.ModelSerializer):
    class Meta:
        model=media
        fields='__all__'


class apm_ser(serializers.ModelSerializer):
    class Meta:
        model=Aprea_memberships
        fields="__all__"


# class orgm_ser(serializers.ModelSerializer):
#     class Meta:
#         model=organization_members
#         fields="__all__"


class person_ser(serializers.ModelSerializer):
    class Meta:
        model=license_Person
        fields="__all__"


class company_ser(serializers.ModelSerializer):
    class Meta:
        model=license_Company
        fields="__all__"


class comment_ser(serializers.ModelSerializer):
    class Meta:
        model=artical_comments
        fields="__all__"