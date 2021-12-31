from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class driverForm(forms.ModelForm):
    class Meta:
        model = driver
        fields = ('email', 'name', 'last_name', 'phone', 'address', 'postcode', 'license_number', 'LN_expiration_date', 'NI', 'birth_date', 'status', 'notes')


class vehicleForm(forms.ModelForm):
    class Meta:
        model = vehicle
        fields = ('plate', 'registered_company_name', 'owner_name', 'make', 'model', 'color', 'cylinder_capacity', 'fuel_type', 'year', 'mileage', 'LOGBOOK_first_date_of_registration', 'mot_expiration_date', 'pco_expiration_date', 'road_tax_expiration_date', 'value', 'rent', 'status', 'notes')


class vehicleDocsForm(forms.ModelForm):
    class Meta:
        model = vehicleDocs
        fields = ('vehicle_id', 'file_name', 'doc')

class driverDocsForm(forms.ModelForm):
    class Meta:
        model = driverDocs
        fields = ('driver_id', 'file_name', 'doc')

class rentalForm(forms.ModelForm):
    class Meta:
        model = rental
        fields = ('driver_id', 'driver_full_name', 'vehicle_id', 'vehicle_plate', 'hire_date', 'return_date', 'deposit', 'balance', 'rent', 'status')


class rentalDocsForm(forms.ModelForm):
    class Meta:
        model = rentalDocs
        fields = ('rental_id', 'file_name', 'doc')


class accountForm(forms.ModelForm):
    class Meta:
        model = account
        fields = ('date','rental_id', 'notes', 'description','value','payment_method','type','in_out')

class ownerForm(forms.ModelForm):
    class Meta:
        model = owner
        fields = ('name', 'start', 'end', 'amount_due', 'amount_paid',)


class ownerDocsForm(forms.ModelForm):
    class Meta:
        model = ownerDocs
        fields = ('owner_account_id', 'file_name', 'doc')

