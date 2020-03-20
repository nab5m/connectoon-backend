from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from account.models import Account, Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Role.objects.all())
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': '비밀번호를 입력해주세요'}
    )

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'name', 'roles']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(AccountSerializer, self).create(validated_data)

    # ToDo: when update password

    def validate(self, data):
        password = data.get('password')
        errors = dict()
        try:
            validate_password(password=password)

        except ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(AccountSerializer, self).validate(data)
