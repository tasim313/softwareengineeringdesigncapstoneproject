from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .forms import FarmerSignUpForm #ProfileForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from App_Shop.models import Product

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Profile


def main(request):
    return render(request, 'App_Farmer/home.html')


def farmer_login_user(request):
    return render(request, 'App_Farmer/farmer_login.html')


def farmer_logout_user(request):
    logout(request)
    messages.warning(request, "You are logged out!!")
    return HttpResponseRedirect(reverse('App_Farmer:farmer-home'))


def farmer_sign_up(request):
    return render(request, 'App_Farmer/farmer_sign_up.html')


class CreateProduct(CreateView):
    model = Product
    template_name = 'App_Shop/create_product.html'
    fields = ('mainimage', 'name', 'category', 'preview_text', 'detail_text', 'price', 'old_price',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def article(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'App_Farmer/article.html', context)


class PostListView(ListView):
     model = Post
     template_name = 'App_Farmer/article.html'
     context_object_name = 'posts'
     ordering = ['-date_posted']
     paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'App_Farmer/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(settings.AUTH_USER_MODEL, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'App_Farmer/create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CreateProfile(CreateView):
    model = Profile
    template_name = 'App_Farmer/create_profile.html'
    fields = ('username', 'full_name', 'profile_pic', 'address_1', 'city', 'zipcode', 'country', 'phone',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def view_profile(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'App_Farmer/profile.html', context)



