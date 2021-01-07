from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('post/<int:id>/<slug:slug>', views.post_detail, name='post_detail' ),
    path('contact/', views.contact, name='contact' ),
    path('about/', views.about, name='about' )
]
