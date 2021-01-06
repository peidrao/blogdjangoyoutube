from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('post/<int:id>/<slug:slug>', views.post_detail, name='post_detail' )
]
