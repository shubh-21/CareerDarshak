from . import views
from django.urls import path
from django.contrib import admin

app_name = 'main'

admin.site.site_header="Career Darshak Admin"
admin.site.site_title="Career Darshak Admin Portal"
admin.site.index_title="Welcome to Career Darshak Admin Portal"



urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.index, name='index'),
    path('project', views.project, name='project'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('prediction', views.prediction, name='prediction'),

]