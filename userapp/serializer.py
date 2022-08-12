
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from main import settings
from .models import User
from django.contrib.auth.models import Group
# from allauth.account.utils import setup_user_email


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    address = serializers.CharField(required=False, write_only=True)
    GROUP_CHOICES = (
        ('customer', 'customer'),
        ('manager', 'manager'),
    )
    group = serializers.ChoiceField(choices=GROUP_CHOICES)
    password1 = serializers.CharField(required=True, write_only=True,label ="Password")
    password2 = serializers.CharField(required=True, write_only=True,label ="Confirm Password")

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'user_type': self.validated_data.get('user_type', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        my_group = Group.objects.get(name=self.validated_data.get('group', '')) 
        my_group.user_set.add(user)
        # setup_user_email(request, user, [])
        return user

        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name',
                  'last_name')
        read_only_fields = ('email', )
