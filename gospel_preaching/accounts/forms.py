from django.forms import CharField, EmailField, RegexField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    username = RegexField(label="Username", max_length=30,
        regex=r'^[\w.+-]+$',
        help_text = "Required. 30 characters or fewer. Letters, digits and ./+/-/_ only.",
        error_messages = {
            'invalid': "This value may contain only letters, numbers and ./+/-/_ characters."})
    email = EmailField()
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    class Meta:
    	model = User
    	fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

class EditProfileForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')
