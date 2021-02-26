from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('portfolio/',  TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]