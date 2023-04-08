from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class UserAuthenticateForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserAuthenticateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = User
        fields = ('email', 'password',)
