from django.shortcuts import redirect, resolve_url
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic
from accounts.forms import LoginForm, SignupForm, UserUpdateForm, MyPasswordChangeForm


# ユーザーモデル取得
User = get_user_model()


# ログインページ
class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


# 自分しかアクセスできないようにするMixin(My Pageのため)
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']


# マイページ
class MyPage(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'accounts/my_page.html'
    # モデル名小文字(user)でモデルインスタンスがテンプレートファイルに渡される


# ログアウト確認用ページ
class LogoutConfirm(generic.TemplateView):
    template_name = "accounts/logout_confirm.html"


# ログアウト完了ページ
class LogoutDone(LogoutView):
    template_name = 'accounts/logout_done.html'


# サインアップページ
class Signup(generic.CreateView):
    template_name = 'accounts/user_form.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save()  # formの情報を保存
        return redirect('accounts:signup_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "アカウント登録"
        return context


# サインアップ完了
class SignupDone(generic.TemplateView):
    template_name = 'accounts/signup_done.html'


# ユーザー登録情報の更新
class UserUpdate(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_form.html'

    def get_success_url(self):
        return resolve_url('accounts:my_page', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Update"
        return context


# パスワード変更
class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/user_form.html'

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "パスワードを変更"
        return context


# パスワード変更完了
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


# 退会確認用
class UserDeleteConfirm(generic.TemplateView):
    template_name = "accounts/delete_confirm.html"


# 退会最終確認
class UserDelete(OnlyYouMixin, generic.DeleteView):
    model = User
    template_name = "accounts/delete.html"
    success_url = reverse_lazy("accounts:delete_done")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Delete"
        return context


# 退会完了
class UserDeleteDone(generic.TemplateView):
    template_name = "accounts/delete_done.html"
