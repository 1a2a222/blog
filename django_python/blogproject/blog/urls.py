from django.conf.urls import url

from . import views
from django.urls import path,include
app_name = 'blog'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('post/<pk>/',views.detail,name='detail'),
# url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    path(r'^archives/<year>/<month>', views.archives, name='archives'),
    path('category/<pk>',views.category,name='category')
    ]