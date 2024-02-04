from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'bio', 'profile_picture']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'bio': forms.Textarea(attrs={'class': 'textarea'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'file-input'}),
        }
