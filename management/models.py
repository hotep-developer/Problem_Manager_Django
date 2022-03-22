from django.db import models
from django.contrib.auth import get_user_model


# ユーザーモデル取得
User = get_user_model()


class Subject(models.Model):  # 教科モデル
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="教科名", max_length=30)

    class Meta:  # 要素の組をもってuniqueとする
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name", ],
                name="subject_unique",
            ),
        ]

    def __str__(self):  # インスタンス名
        return self.name


class Book(models.Model):  # 問題集モデル
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(
        Subject, verbose_name="教科", on_delete=models.CASCADE, related_name="books")
    name = models.CharField(verbose_name="問題集", max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "subject", "name", ],
                name="book_unique"
            ),
        ]

    def __str__(self):
        return self.name


class Problem(models.Model):  # 問題モデル
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # subject = models.ForeignKey(Subject, verbose_name="教科", on_delete=models.CASCADE, related_name="problems")
    book = models.ForeignKey(Book, verbose_name="問題集",
                             on_delete=models.CASCADE, related_name="problems",)
    number = models.PositiveIntegerField(verbose_name="問題番号")
    CHECKS = (
        (1, "✕"),
        (2, "◯"),
    )
    checker = models.IntegerField(
        verbose_name="チェック", choices=CHECKS, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "book", "number", ],
                name="problem_unique"
            ),
        ]

    def __str__(self):
        return str(self.number)
