from django.urls import path
from accounts import views


app_name = "accounts"

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("my_page/<int:pk>/", views.MyPage.as_view(), name="my_page"),
    path("logout_confirm/", views.LogoutConfirm.as_view(), name="logout_confirm"),
    path("logout_done/", views.LogoutDone.as_view(), name="logout_done"),
    path("signup/", views.Signup.as_view(), name="signup"),
    path("signup_done/", views.SignupDone.as_view(), name="signup_done"),
    path("user_update/<int:pk>/", views.UserUpdate.as_view(), name="user_update"),
    path("password_change/", views.PasswordChange.as_view(), name="password_change"),
    path("password_change_done/", views.PasswordChangeDone.as_view(),
         name="password_change_done"),
    path("delete_confirm/", views.UserDeleteConfirm.as_view(), name="delete_confirm"),
    path("delete/<int:pk>/", views.UserDelete.as_view(), name="delete"),
    path("delete_done/", views.UserDeleteDone.as_view(), name="delete_done"),
]
