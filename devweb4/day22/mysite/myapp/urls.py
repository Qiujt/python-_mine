from django.conf.urls  import url
from . import  views

urlpatterns = [
    url(r'^hello/$',views.hello,{'age':23},name='hello'),
    url(r'^(?P<name>[a-zA-Z]+)/(?P<age>\d+)/', views.info, name='info'),
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^protect/$', views.protect, name='protect'),
    url(r'^login/$', views.login, name='login'),
    url(r'^template/$',views.template,name='template'),

]