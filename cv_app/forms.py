from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'profession', 'education', 'experience', 'skills', 'languages', 'website', 'bio', 'profile_picture']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'profession': forms.Textarea(attrs={'class': 'textarea', 'rows': 3}),
            'education': forms.Textarea(attrs={'class': 'textarea', 'rows': 3}),
            'experience': forms.Textarea(attrs={'class': 'textarea', 'rows': 3}),
            'skills': forms.Textarea(attrs={'class': 'textarea', 'rows': 3}),
            'languages': forms.Textarea(attrs={'class': 'textarea', 'rows': 3}),
            'website': forms.Textarea(attrs={'class': 'textarea', 'rows': 3}),
            'bio': forms.Textarea(attrs={'class': 'textarea', 'rows': 3}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'file-input'}),
        }
