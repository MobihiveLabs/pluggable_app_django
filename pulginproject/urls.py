from django.contrib import admin
from django.urls import path
from agent.views import agent_form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',agent_form_view, name='combined')
]
