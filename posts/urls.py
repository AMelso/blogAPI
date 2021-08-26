from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    ## default path posts/
    path('', views.PostListView.as_view(), name='post-list'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('<slug>/', views.PostDetailView.as_view(), name='post-detail'),

]