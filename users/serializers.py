from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email']

    def create(self, validated_data):
        """
        Создание нового пользователя с заданными параметрами
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновление данных существующего пользователя
        """
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
