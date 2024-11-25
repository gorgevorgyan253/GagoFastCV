from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Resume, Skill, Experience, Education, Language

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = [SkillInline, ExperienceInline, EducationInline, LanguageInline]

admin.site.register(Resume, ResumeAdmin)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Language)
