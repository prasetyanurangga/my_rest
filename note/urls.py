from note import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('note/', views.note_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)