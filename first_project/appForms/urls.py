from django.conf.urls import url
from appForms import views

urlpatterns = [
    # url('', views.index, name='index'),
    url('', views.formPage, name='formPage'),
]