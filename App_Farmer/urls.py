from django.urls import path

from . import views
from .views import CreateProduct, CreateProfile

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

app_name = 'App_Farmer'

urlpatterns = [
    path('', views.main, name='farmer-home'),
    path('farmer/login/', views.farmer_login_user, name='farmer-login'),
    path('farmer/logout/', views.farmer_logout_user, name='farmer-logout'),
    path('farmer/signup/', views.farmer_sign_up, name='farmer-signup'),
    path('product/new/', CreateProduct.as_view(), name='Product-create'),
    path('article/', PostListView.as_view(), name='farmer-article'),
    path('view_profile/', views.view_profile, name='farmer-view-profile'),
    path('farmer/profile/', CreateProfile.as_view(), name='farmer-profile'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]


