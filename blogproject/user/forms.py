from django import forms
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter first name'
        }
    ))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter last name'
        }
    ))
    email = forms.EmailField(max_length=128, widget=forms.EmailInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Email email'
        }
    ), )
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Enter password'
        }
    ))
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Confirm password'
        }
    ))

    profile_pic = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': "form-control",
        }
    ))


    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'profile_pic', 'password', 'confirm_password']

    def clean_confirm_password(self):
        """
        Confirming the password is typed correctly.
        Checking two passwords match.
        """
        cleaned_data = super(UserRegistrationForm, self).clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')
        if password1 != password2:
            raise forms.ValidationError("Passwords do no match")

        return cleaned_data

    def save(self, commit=True):
        """ overriding default save method of modelform
            so that it calls the create_user method instead of just create.
            This is needed incase, password do not get hashed by using default create method.
        """
        user = CustomUser.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            profile_pic=self.cleaned_data['profile_pic'],
        )
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        max_length=128,
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'placeholder': 'Email'
            }
        )
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': 'password'
            }
        )
    )