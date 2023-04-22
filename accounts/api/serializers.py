from rest_framework import serializers
from ..models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "age",
            "skin_tone",
            "body_shape",
            "mobile_number"
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser(**validated_data)
        user.set_password(password)
        user.save()
        return user