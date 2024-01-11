from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username','location','voice','bio','profile_image','social_facebook','social_instagram','social_twitter','social_youtube','social_website']
        labels = {
            'name':'Imię i nazwisko',
            'username':'Nazwa użytkownika',
            'location':'Miejsce zamieszkania',
            'voice':'Głos w chórze',
            'bio':'O sobie',
            'profile_image':'Zdjęcie profilowe',
            'social_facebook':'Link do serwisu Facebook',
            'social_instagram':'Link do serwisu Instagram',
            'social_twitter':'Link do serwisu Twitter',
            'social_youtube':'Link do serwisu Youtube',
            'social_website':'Link do prywatnej strony',
        }
        

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})