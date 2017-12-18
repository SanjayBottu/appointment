from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import EmployeeForm
from .models import Employee,Client,Appointment,Schedule,Service



# def create(request):
#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#                 emp_item = form.save(commit=False)
#                 emp_item.save()
#     else:
#         emp_form = EmployeeForm()
#     return render(request, 'appointment/emp_form.html',{'form':form})

class EmployeeList(ListView):
    model = Employee

class EmployeeInsert(CreateView):
    model = Employee
success_url = reverse_lazy('employee_list')
fields = ['first_name', 'last_name', 'merchant_username']

class EmployeeUpdate(UpdateView):
    model = Employee
success_url = reverse_lazy('employee_list')
fields = ['first_name', 'last_name', 'merchant_username']

class EmployeeDelete(DeleteView):
    model = Employee
success_url = reverse_lazy('employee_list')

