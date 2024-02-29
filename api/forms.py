from database.models import User, Messages, Customer, Organization

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import FilteredSelectMultiple


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name'
    }))
    tg_id = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'placeholder': 'Telegram ID'
    }))
    tg_nickname = forms.CharField(required=False, max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Telegram nickname'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))

    class Meta:
        model = User
        fields = ['full_name', 'tg_id', 'tg_nickname', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MessagesForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ['sender_type', 'source', 'message']

    sender_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'size': 10}))
    source = forms.CharField(required=False, widget=forms.TextInput(attrs={'size': 10}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['full_name', 'tg_id', 'tg_nickname', 'organizations']

    full_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    tg_id = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Telegram ID'}),
    )
    tg_nickname = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Telegram nickname'}),
    )
    organizations = forms.ModelMultipleChoiceField(
        label='',
        queryset=Organization.objects.all(),
        widget=FilteredSelectMultiple("Organizations",
                                      is_stacked=False),
        required=False,
    )
