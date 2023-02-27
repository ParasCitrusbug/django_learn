from django import forms


class feedbackform(forms.Form):
    email = forms.EmailField(label="Enter email", max_length=100)
    name = forms.CharField(label="Enter name", max_length=100)
    email = forms.CharField(label="your feedback", widget=forms.Textarea)
