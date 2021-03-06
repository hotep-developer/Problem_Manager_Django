# from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from management.models import Subject, Book, Problem
from management.forms import SubjectForm, BookForm, ProblemForm



def top(request):
    # topページ
    subjects = Subject.objects.filter(user=request.user).all().order_by("name")
    books_count = Book.objects.filter(user=request.user).all().count()
    context = {
        "subjects":subjects,
        "books_count":books_count,
    }
    return render(request, "management/top.html", context)


def index(request):
    # Subject Book 一覧
    subjects = Subject.objects.filter(user=request.user).all().order_by("name")

    context = {
        "subjects":subjects,
    }
    return render(request, "management/index.html", context)


def subject_create(request):
    # Subject 作成 (function base)
    if request.method == "POST":
        form = SubjectForm(request.POST, initial={"user":request.user}) # 初期値ありでフォームを作成
        if form.is_valid():
            # subject = form.save(commit=False)
            # subject.user = request.user
            # subject.save()
            form.save()
            return redirect("management:index")
    else:
        form = SubjectForm(initial={"user":request.user})
    context = {
        "process": "作成",
        "object_kind": "教科",
        "form": form,
        "url_cancel": reverse("management:index"),
    }
    return render(request, "management/management_form.html", context=context)


# def subject_index(request): # 教科一覧
#     subjects = Subject.objects.filter(user=request.user).all().order_by("name")

#     context = {
#         "subjects":subjects,
#     }
#     return render(request, "management/subject_index.html", context)


# class SubjectCreate(generic.CreateView):
#     # Subject 作成 (calss base)
#     form_class = SubjectForm
#     template_name = "management/management_form.html"

#     def get_initial(self): # 初期値
#           initial = super().get_initial()
#           initial["user"] = self.request.user # ユーザー欄だけ初期値あり
#           return initial

#     def form_valid(self, form):  # POSTのときの挙動
#         subject = form.save(commit=False)  # formの情報を保存
#         subject.save() # get_init で初期値が入っているので,userは勝手にコミットされる
#         return redirect("management:subjects")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["process"] = "作成"
#         context["object_kind"] = "教科"
#         context["url_cancel"] = reverse("management:subjects")
#         return context


def subject_detail(request, pk):
    # Subject 詳細(detail & update)用
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect("management:index")
    else:
        form = SubjectForm(instance=subject)
    context = {
        "process": "更新",
        "object_kind": "教科",
        "form": form,
        "url_cancel": reverse("management:index"),
        "url_delete": reverse("management:subject_delete", args=(subject.pk,)),
    }
    return render(request, "management/management_form.html", context=context)


def subject_delete(request, pk):
    # Subject 削除用
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        subject.delete()
        return redirect("management:index")
    context ={
        "process": "削除",
        "object_kind": "教科",
        "object": subject,
        "url_cancel": reverse("management:subject_detail", args=(subject.pk, )),
    }
    return render(request, "management/delete_confirm.html", context)


def book_create(request):
    # Book 作成用
    if request.method == "POST":
        form = BookForm(request.POST,initial={"user":request.user}) # 初期値ありでフォームを作成
        # form.fields["subject"].queryset = form.fields["subject"].queryset.filter(user=request.user) # こっちはいらないかも
        if form.is_valid():
            form.save()
            return redirect("management:index")
    else:
        form = BookForm(initial={"user":request.user})
        form.fields["subject"].queryset = form.fields["subject"].queryset.filter(user=request.user)
    context = {
        "process": "作成",
        "object_kind": "問題集",
        "form": form,
        "url_cancel": reverse("management:index"),
    }
    return render(request, "management/management_form.html", context=context)


def book_detail(request, pk):
    # Book 詳細(detail & update)用
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST,instance=book) # 初期値ありでフォームを作成
        if form.is_valid():
            form.save()
            return redirect("management:index")
    else:
        form = BookForm(instance=book)
        form.fields["subject"].queryset = form.fields["subject"].queryset.filter(user=request.user)
    context = {
        "process": "更新",
        "object_kind": "問題集",
        "form": form,
        "url_cancel": reverse("management:index"),
        "url_delete": reverse("management:book_delete", args=(book.pk,)),
    }
    return render(request, "management/management_form.html", context=context)


def book_delete(request, pk):
    # Book 削除用
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("management:index")
    context ={
        "process": "削除",
        "object_kind": "問題集",
        "object": book,
        "url_cancel": reverse("management:book_detail", args=(book.pk, )),
    }
    return render(request, "management/delete_confirm.html", context)


def problem_create(request):
    # Problem 作成用
    if request.method == "POST":
        # form = ProblemForm(request.POST) # 初期値ありでフォームを作成
        form = ProblemForm(request.POST, initial={"user":request.user}) # 初期値ありでフォームを作成
        if form.is_valid():
            form.save()
            return redirect("management:top")
    else:
        # form = ProblemForm()
        form = ProblemForm(initial={"user":request.user})
        # form.fields["subject"].queryset = form.fields["subject"].queryset.filter(user=request.user)
        form.fields["book"].queryset = form.fields["book"].queryset.filter(user=request.user)
    context = {
        "process": "作成",
        "object_kind": "問題",
        "form": form,
        "url_cancel": reverse("management:top"),
    }
    return render(request, "management/management_form.html", context=context)


def problem_detail(request, pk):
    # Problem 詳細(detail & update)用
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == "POST":
        form = ProblemForm(request.POST,instance=problem) # 初期値ありでフォームを作成
        if form.is_valid():
            form.save()
            return redirect("management:top")
    else:
        form = ProblemForm(instance=problem)
        form.fields["book"].queryset = form.fields["book"].queryset.filter(user=request.user)
    context = {
        "process": "更新",
        "object_kind": "問題",
        "form": form,
        "url_cancel": reverse("management:top"),
        "url_delete": reverse("management:problem_delete", args=(problem.pk,)),
    }
    return render(request, "management/management_form.html", context=context)


def problem_delete(request, pk):
    # Problem 削除用
    problem = get_object_or_404(Problem, pk=pk)
    if request.method == "POST":
        problem.delete()
        return redirect("management:top")
    context ={
        "process": "削除",
        "object_kind": "問題",
        "object": problem,
        "url_cancel": reverse("management:problem_detail", args=(problem.pk, )),
    }
    return render(request, "management/delete_confirm.html", context)