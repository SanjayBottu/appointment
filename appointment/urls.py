from django.conf.urls import url
# from django.views.generic import DetailView, ListView, UpdateView
# from models import Restaurant, Dish
# from forms import RestaurantForm, DishForm
# from views import RestaurantCreate, DishCreate, RestaurantDetail
from . import views

urlpatterns = [
    url(r'^$', views.EmployeeList.as_view(), name='employee_list'),
    url(r'^insert$', views.EmployeeInsert.as_view(), name='employee_insert'),
    url(r'^update/(?P<pk>\d+)$', views.EmployeeUpdate.as_view(), name='employee_update'),
    url(r'^delete/(?P<pk>\d+)$', views.EmployeeDelete.as_view(), name='employee_delete')
]

