from django import forms
from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    reading_date = forms.DateField(
        label='독서일',
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date'
        })
    )
    class Meta:
        model = Thread
        exclude = ["cover_img", "likes", "user", "book", "created_at", "updated_at"]

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'id_content',
            'placeholder': '댓글을 입력하세요',
            'class': 'form-control',  # 부트스트랩 적용 시
        }),
        label='',  # 라벨 제거 (원하면)
    )

    class Meta:
        model = Comment
        exclude = ('user', 'thread', "created_at", "updated_at")