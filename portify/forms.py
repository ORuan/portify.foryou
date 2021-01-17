from django.forms import ModelForm
from django import forms
from portify.models import Experience, Skills, Portify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForms(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ExperienceForms(ModelForm):
    class Meta:
        model = Experience
        fields = ['_local',
                  'when_started',
                  'when_end',
                  'job']

class SkillsForms(ModelForm):
    class Meta:
        model = Skills
        fields = ['skill_name',
                  'exp_time']

class PortifyForms(ModelForm):
    class Meta:
        model = Portify
        fields = ['name',
                  'email',
                  'link_github',
                  'link_linkedin',
                  'avatar']