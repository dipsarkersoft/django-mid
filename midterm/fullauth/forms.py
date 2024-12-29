from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class Register_User(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

    def __str__(self):
        return self.first_name 
       




class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']       