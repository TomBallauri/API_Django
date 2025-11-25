from rest_framework.serializers import ModelSerializer

from authentication.models import AuthorUser


class AuthorUserSerializer(ModelSerializer):
    class Meta:
        model = AuthorUser
        fields = [
            "id",
            "username",
            "password",
        ]
        extra_kwargs = {
         'password': {'write_only': True}
        }

    def create(self, validated_data):

        password = validated_data.pop('password')
        user = AuthorUser(**validated_data)
        user.set_password(password)
        user.save()

        return user