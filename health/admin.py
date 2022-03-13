from django.contrib import admin

from .models import Symptom, Submission, UserSymptom


class UserSymptomInline(admin.TabularInline):
    model = UserSymptom
    raw_id_fields = ['submisson']


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    pass


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    inlines = [UserSymptomInline]
