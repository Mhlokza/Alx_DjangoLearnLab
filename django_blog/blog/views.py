from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView, CreateView,TemplateView
from django.contrib import auth
from .forms import ProfileForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    context_object_name = 'form'

class LoginUserViews(LoginView):
    template_name= 'blog/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

def LogoutUserView(request):
    auth.logout(request)
    return redirect('login')

def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.post, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form = ProfileForm(instance = request.user)
        return render(request,'blog/profile.html', {'form': form})

class ListView(ListAPIView):
    list = Post.object.all()

class DetailView(DetailAPIView):
    detail = Post.object.all()

class CreateView(CreateAPIView):
    create = Post.object.all()

class UpdateView(UpdateAPIView):
    update = Post.object.all()

class DeleteView(DeleteAPIView):
    delete = Post.object.all()


    
    




