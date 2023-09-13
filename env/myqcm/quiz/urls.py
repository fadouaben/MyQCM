from django.urls import path
from . import views
urlpatterns = [
    path('create_qcm/',views.create_qcm,name='create_qcm'),
]