from urllib.parse import urlparse
from django.urls import path
from .views import BlogDetailView, BlogUpdateView, blogListView, BlogCreateView, BlogDeleteView

app_name="blog"

urlpatterns = [
    path('', blogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete")

]