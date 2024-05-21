from rest_framework import serializers

from user.models import CustomUser


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)
    re_password = serializers.CharField(min_length=8, max_length=128, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 're_password', 'email', 'date_joined')
        read_only_fields = ('id', 'date_joined')

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('re_password'):
            raise serializers.ValidationError({'password': 'passwords are not the same!'})
        return attrs

    def create(self, validated_data):
        instance = CustomUser.objects.create_user(username=validated_data['username'],
                                                  password=validated_data['password'],
                                                  email=validated_data['email'])
        return instance
