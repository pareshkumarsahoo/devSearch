from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.projects, name='projects'),
    path('project/<int:id>/', v.project, name='project')
]
