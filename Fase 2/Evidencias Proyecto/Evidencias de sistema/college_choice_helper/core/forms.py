from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError

class MiSetPasswordForm(SetPasswordForm):
    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')

        return password
    
    def clean_new_password2(self):
        password2 = self.cleaned_data.get('new_password2')
        
        return password2
