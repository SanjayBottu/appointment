from django.db import models


class Employee(models.Model) :
    #uuid employee
    employee_id = models.UUIDField(unique=True, null=True, blank=True, editable=False)
    first_name = models.CharField(max_length=64,unique=True)
    last_name = models.CharField(max_length=64)
    #merchant_email_id...merchant_username =  models.CharField(max_length=255, blank=False, null=False)
    merchant_username =  models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.first_name


class Schedule(models.Model) :
    employee_name = models.ForeignKey(Employee, to_field="first_name", db_column="first_name", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Client(models.Model) :
    client_id = models.UUIDField(unique=True, null=True, blank=True, editable=False)
    #client_name = models.CharField(max_length=128)...client_username =  models.CharField(max_length=255, blank=False, null=False, default='admin')
    client_username =  models.CharField(max_length=255, unique=True, blank=False, null=False)
    #THis can be dundeal user or it can be merchants own client
    contact_phone = models.CharField(max_length=128, null='false')
    contact_email = models.EmailField(max_length=128, null='false')

    def __str__(self):
        return self.client_username

class Appointment(models.Model) :
    appointment_id = models.UUIDField(unique=True, null=True, blank=True, editable=False)
    created = models.DateTimeField(blank=True, null=True)
    employee_created = models.ForeignKey(Employee, null=True, blank=True, to_field="first_name", db_column="first_name", on_delete=models.CASCADE)
    client = models.ForeignKey(Client, null=True, blank=True, to_field="client_username", db_column="client_username", on_delete=models.CASCADE)
    client_name = models.CharField(max_length=128)
    client_contact = models.CharField(max_length=128)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time_expect = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    price_expected = models.DecimalField(max_digits=10,decimal_places=2)
    price_full = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.DecimalField(max_digits=10,decimal_places=2)
    price_final = models.DecimalField(max_digits=10,decimal_places=2)
    cancelled = models.BooleanField(default=False)
    cancellation_reason = models.TextField(default=False)

    def __str__(self):
        return self.client_name


class Service(models.Model) :
    service_id = models.UUIDField(unique=True, null=True, blank=True, editable=False)
    service_name = models.CharField(max_length=128,unique=True)
    duration = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.service_name

class Service_provided(models.Model) :
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, blank=True, to_field="service_name", db_column="service_name", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)

class Service_booked(models.Model) :
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, blank=True, to_field="service_name", db_column="service_name", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)



