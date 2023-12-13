from django import forms


class AddForm(forms.Form):
    post_name = forms.CharField(max_length=100)
    post_description = forms.CharField(max_length=5000)
    post_img = forms.URLField()