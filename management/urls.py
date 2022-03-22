from django.urls import path
from management import views


app_name = "management"

urlpatterns = [
    # topページ関係
    path("", views.top, name="top"),
    # 教科・問題集 一覧
    path("index/", views.index, name="index"),
    # Subject 関係
    path("subject/create/", views.subject_create, name="subject_create"),
    path("subject/<int:pk>/detail/", views.subject_detail, name="subject_detail"),
    path("subject/<int:pk>/delete/", views.subject_delete, name="subject_delete"),
    # Book 関係
    path("book/create/", views.book_create, name="book_create"),
    path("book/<int:pk>/detail/", views.book_detail, name="book_detail"),
    path("book/<int:pk>/delete/", views.book_delete, name="book_delete"),
    # Problem 関係
    path("problem/create/", views.problem_create, name="problem_create"),
]
