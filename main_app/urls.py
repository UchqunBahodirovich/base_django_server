
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('getByName/<int:id>', views.GetByScientistId.as_view()),
    path('getByName/<str:full_name>', views.GetByScientistName.as_view()),
    path('getAll/', views.GetAllScientistName.as_view())

]
urlpatterns = format_suffix_patterns(urlpatterns)