from lists import views
from django.urls import path, re_path

urlpatterns = [
    path('new', views.new_list, name='new_list'),
    re_path(r'^(\d+)/$', views.view_list, name='view_list'),
    re_path(r'^(\d+)/add_items$', views.add_item, name='add_item'),
]
