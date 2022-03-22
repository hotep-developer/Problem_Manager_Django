from django.contrib.auth import get_user_model
from django import forms

from management.models import Subject, Book, Problem

# ユーザーモデルの取得
User=get_user_model()




class SubjectForm(forms.ModelForm):
    # Subject のフォーム

    class Meta:
        model = Subject
        fields = ("user", "name", )

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields["user"].disabled = True # ユーザー欄は操作不可
        # self.fields["user"].widget = forms.HiddenInput()
        self.fields["user"].label = "ユーザー" #


class BookForm(forms.ModelForm):
    # Book のフォーム
    # "user"フィールドのquerysetのフィルタリングはview側でやってる。
    # たぶん効率わるい
    class Meta:
        model = Book
        fields = ("user", "subject", "name", )

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields["user"].disabled = True # ユーザー欄は操作不可
        self.fields["user"].label = "ユーザー"


class ProblemForm(forms.ModelForm):
    # Problem のフォーム
    class Meta:
        model = Problem
        fields = ("user", "book", "number", "checker", )

    def __init__(self, *args, **kwargs):
        super(ProblemForm, self).__init__(*args, **kwargs)
        self.fields["user"].disabled = True # ユーザー欄は操作不可
        self.fields["user"].label = "ユーザー"
