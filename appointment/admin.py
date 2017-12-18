from django.contrib import admin
from .models import Schedule,Employee,Client,Appointment,Service

admin.site.register(Schedule)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Service)