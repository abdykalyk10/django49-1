from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms

class RegisterView(CreateView):
    form_class = forms.CustomRegisterForm
    template_name = 'work_age/register.html'
    success_url = reverse_lazy('work_age:login')


class AuthloginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'work_age/login.html'

    def get_success_url(self):
        return reverse_lazy('work_age:work_age_login')

class AuthLogoutView(LoginView):
    next_page = reverse_lazy('work_age:login')

class UsersListView(ListView):
    template_name = 'work_age/user_list.html'
    context_object_name = 'person'
    model = models.CustomUser

    def get_queryset(self):
        return models.CustomUser.objects.all()

    def get_success_url(self):
        return reverse_lazy('work_age:user_list')