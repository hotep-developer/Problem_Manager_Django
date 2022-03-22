from django.contrib.auth import get_user_model
from django import forms

from management.models import Book, Subject

# ユーザーモデルの取得
User=get_user_model()




# 教科フォーム
class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ("user", "name", )

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields["user"].disabled = True # ユーザー欄は操作不可
        # self.fields["user"].widget = forms.HiddenInput()
        self.fields["user"].label = "ユーザー" #





class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("user", "subject", "name", )

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields["user"].disabled = True # ユーザー欄は操作不可
        self.fields["user"].label = "ユーザー"
