from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from auth_system.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone_number', 'first_name')


class CustomAuthenticationForm(AuthenticationForm):
    ...