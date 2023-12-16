from django import forms


class AddForm(forms.Form):


    post_name = forms.CharField(max_length=100)
    post_description = forms.CharField(max_length=5000)
    post_img = forms.URLField()
    popular = forms.CharField(max_length=3)

class UserForm(forms.Form):
    email = forms.EmailField(required=False, label="Введите email")
    password = forms.CharField(label='Введите пароль')


class Comment(forms.Form):
    Comment = forms.CharField(max_length=50)
    like = forms.CharField(max_length=3)