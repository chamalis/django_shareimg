from django.conf.urls import include, url
import views

urlpatterns = [ 
    url(r'^$', views.index, name="main"),
    url(r'^upload/$', views.handle_upload, name="upload"),
]
