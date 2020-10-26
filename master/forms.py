from django import forms

class RoomNameForm(forms.Form):
    room_name = forms.CharField(label='Room name', max_length=100)
    password = forms.CharField(label='Room password',widget=forms.PasswordInput)