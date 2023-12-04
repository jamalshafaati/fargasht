from django import forms
from .models import Comment,News



class CommentForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control" ,'name':"name" ,'autocomplete':"off", 'placeholder':"نام", 'data-bv-field':"name" ,'type':"text"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control" ,'name':"email", 'autocomplete':"off" ,'placeholder':"ایمیل" ,'data-bv-field':"email", 'type':"email"}))
    body=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control textarea" ,'rows':"3", 'name':"message", 'placeholder':"پیام", 'data-bv-field':"message"}))

    class Meta:
        model=Comment
        fields=('name','email','body')
class News_Form(forms.ModelForm):

    class Meta:
        model=News
        fields=('title','body','Image')
