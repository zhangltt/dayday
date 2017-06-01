from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^register/$',views.register),
    url(r'info/$', views.info),
    url(r'order/$', views.order),
    url(r'site/$', views.site),

]