from django.forms import CharField, EmailField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class NewUserForm(UserCreationForm):
    email = EmailField()
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)

class EditProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')
