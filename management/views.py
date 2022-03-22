from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from management.models import Book, Problem, Subject
from management.forms import SubjectForm, BookForm



def index(request): # 問題一覧
    subjects = Subject.objects.filter(user=request.user).all().order_by("name")
    context = {
        "subjects":subjects,
    }
    return render(request, "management/index.html", context)


def subject_index(request): # 教科一覧
    subjects = Subject.objects.filter(user=request.user).all().order_by("name")

    context = {
        "subjects":subjects,
    }
    return render(request, "management/subject_index.html", context)


# class SubjectCreate(generic.CreateView): # 教科作成 (calss base)
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

def subject_create(request): # 教科作成 (function base)
    if request.method == "POST":
        form = SubjectForm(request.POST, initial={"user":request.user}) # 初期値ありでフォームを作成
        if form.is_valid():
            # subject = form.save(commit=False)
            # subject.user = request.user
            # subject.save()
            form.save()
            return redirect("management:subjects")
    else:
        form = SubjectForm(initial={"user":request.user})
    context = {
        "process": "作成",
        "object_kind": "教科",
        "form": form,
        "url_cancel": reverse("management:subjects"),
    }
    return render(request, "management/management_form.html", context=context)


def subject_detail(request, pk): # 教科詳細
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect("management:subjects")
    else:
        form = SubjectForm(instance=subject)
    context = {
        "process": "更新",
        "object_kind": "教科",
        "form": form,
        "url_cancel": reverse("management:subjects"),
        "url_delete": reverse("management:subject_delete", args=(subject.pk,)),
    }
    return render(request, "management/management_form.html", context=context)


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        subject.delete()
        return redirect("management:subjects")
    context ={
        "process": "削除",
        "object_kind": "教科",
        "object": subject,
        "url_cancel": reverse("management:subject_detail", args=(subject.pk, )),
    }
    return render(request, "management/delete_confirm.html", context)


def book_index(request): # 教科一覧
    subjects = Subject.objects.filter(user=request.user).all().order_by("name")

    context = {
        "subjects":subjects,
    }
    return render(request, "management/book_index.html", context)

def book_create(request): # 問題集作成 (function base)
    if request.method == "POST":
        form = BookForm(request.POST,initial={"user":request.user}) # 初期値ありでフォームを作成
        if form.is_valid():
            # subject = form.save(commit=False)
            # subject.user = request.user
            # subject.save()
            form.save()
            return redirect("management:book_index")
    else:
        form = BookForm(initial={"user":request.user})
    context = {
        "process": "作成",
        "object_kind": "問題集",
        "form": form,
        "url_cancel": reverse("management:book_index"),
    }
    return render(request, "management/management_form.html", context=context)