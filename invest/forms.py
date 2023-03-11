from django.forms import ModelForm
from invest.models import User

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", 'first_name', 'last_name' ,'email', 'password', )

        def save(self, commit=True):
            user = super().save(commit)
            user.set_password(self.cleaned_data['password'])
            user.save()
            return user