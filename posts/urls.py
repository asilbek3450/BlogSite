from django.urls import path

from .views import posts, post_detail, base_navbar

urlpatterns = [
    path('', posts, name='posts'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    # path('about/', about, name='about'),
    path('base/', base_navbar, name='base_navbar'),
    ]
