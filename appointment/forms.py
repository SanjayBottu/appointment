from django.forms import ModelForm
from  .models import Appointment,Employee,Client


class EmployeeForm(ModelForm) :
    class Meta:
        empmodel = Employee
        fields = ['first_name','last_name']
