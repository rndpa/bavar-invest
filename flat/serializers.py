from .models import *
from rest_framework import serializers


class FlatListSerializer(serializers.ModelSerializer):
    main_country = serializers.StringRelatedField()
    main_city = serializers.StringRelatedField()
    main_type_real_estate = serializers.StringRelatedField()
    main_rooms = serializers.StringRelatedField()
    main_offer = serializers.StringRelatedField()
    main_district = serializers.StringRelatedField()
    main_status = serializers.StringRelatedField()
    main_infrastructure = serializers.StringRelatedField()

    class Meta:
        model = Flat
        fields = '__all__'
