from django.urls import path,include
from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/post/<post_pk>',views.post_comment,name='post_comment'),

]