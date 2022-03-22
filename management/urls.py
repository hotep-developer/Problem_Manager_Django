from django.urls import path
from management import views


app_name = "management"

urlpatterns = [
    path("", views.index, name="index"),
    # Subject関係
    path("subjects/", views.subject_index, name="subjects"),
    # path("subjects/create/", views.SubjectCreate.as_view(), name="subject_create"), # クラスベースviewの場合
    path("subjects/create/", views.subject_create, name="subject_create"),
    path("subjects/<int:pk>/detail/", views.subject_detail, name="subject_detail"),
    path("subjects/<int:pk>/delete/", views.subject_delete, name="subject_delete"),
    # Book関係 (Subjectからurlの書き方を変更)
    path("book/index/", views.book_index, name="book_index"),
    path("book/create/", views.book_create, name="book_create"),
    path("book/<int:pk>/detail/", views.book_detail, name="book_detail"),
    path("book/<int:pk>/delete/", views.book_delete, name="book_delete"),
]
