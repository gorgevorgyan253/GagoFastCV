from django.urls import path
from . import views

urlpatterns = [
    path('resume/step-1/', views.resume_step_1, name='resume_step_1'),
    path('resume/step-2/', views.resume_step_2, name='resume_step_2'),
    path('resume/step-3/', views.resume_step_3, name='resume_step_3'),
    path('resume/step-4/', views.resume_step_4, name='resume_step_4'),
    path('resume/step-5/', views.resume_step_5, name='resume_step_5'),
    path('resume/step-6/', views.resume_step_6, name='resume_step_6'),
    path('resume/step-7/', views.resume_step_7, name='resume_step_7'),
    path('resume/review/', views.resume_review, name='resume_review'),
    path('resume/success/', views.resume_success, name='resume_success'),
]
