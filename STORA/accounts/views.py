from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from STORA.accounts.forms import CustomUserCreationForm
from STORA.accounts.models import Employee


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'accounts/employee_list.html'
    context_object_name = 'employees'


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'accounts/employee_details.html'
    context_object_name = 'employee'


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    template_name = 'accounts/employee_edit.html'
    fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'role']
    context_object_name = 'employee'

    def get_success_url(self):
        return reverse_lazy('employee_details', kwargs={'pk': self.object.pk})


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'accounts/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')
    context_object_name = 'employee'