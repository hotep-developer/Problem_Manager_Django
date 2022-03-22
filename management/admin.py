from django.contrib import admin

from management.models import Subject, Book, Problem

admin.site.register([Subject, Book, Problem])
