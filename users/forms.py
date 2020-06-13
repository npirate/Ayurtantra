from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser #or from django.contrib.auth import get_user_model and use get_user_model() in place of CustomUser

class CustomUserCreationForm (UserCreationForm):
    class Meta (UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ('age',) will show only username, age and password fields
        fields = ('username', 'email',) #will show fields that are explicitely defined here.

class CustomUserChangeForm (UserChangeForm):
    class Meta (UserChangeForm.Meta):
        model = CustomUser
        #fields = UserChangeForm.Meta.fields  will show only username and password fields
        fields = ('username', 'email',)  #will show fields that are explicitely defined here.