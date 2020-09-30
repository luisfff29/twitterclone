from django import forms


class TweetForm(forms.Form):
    body = forms.CharField(max_length=140, widget=forms.Textarea(
        attrs={
            'class': 'form-control my-3 bg-tweet text-white',
            'placeholder': "What's happening?",
            'rows': '5'
        }
    ))


class CommentForm(forms.Form):
    body = forms.CharField(max_length=140, widget=forms.Textarea(attrs={
        'class': 'form-control bg-tweet text-white',
        'placeholder': 'Write a comment...',
        'rows': '1',
    }))
