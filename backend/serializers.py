from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializers(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get_id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name


# class UserSerializerWithToken(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']
#
#     def get_token(self, obj):
#         token =

class ReviewSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSeralizer(reviews, many=True)
        return serializer.data
