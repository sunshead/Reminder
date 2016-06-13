from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Appointment
from django.shortcuts import render

# Create your views here.
class AppointmentCreateView(SuccessMessageMixin, CreateView):

	model = Appointment
	fields = ['name', 'phone_number', 'time', 'time_zone']
	success_message = 'Successfully created appointment.'