from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', login_page, name='login_page'),

    path('login', login_page, name='login_page'),
    path('signup', signup, name='signup'),
    path('logout', logout_page, name="logout_page"),

    url(r'^$', home, name='display'),
    path('home', home, name='display'),
    path('download/<path:path>', download, name='download'),

    path('vehicles', vehicles, name="vehicles"),
    path('view_vehicle/<int:vehicle_id>', view_vehicle, name="view_vehicle"),
    path('edit_vehicle/<int:vehicle_id>', edit_vehicle, name="edit_vehicle"),
    path('add_vehicle', add_vehicle, name="add_vehicle"),
    path('delete_vehicle/<int:vehicle_id>', delete_vehicle, name="delete_vehicle"),
    path('delete_vehicleDoc/<int:vehicleDoc_id>', delete_vehicleDoc, name="delete_vehicleDoc"),


    path('drivers', drivers, name="drivers"),
    path('view_driver/<int:driver_id>', view_driver, name="view_driver"),
    path('edit_driver/<int:driver_id>', edit_driver, name="edit_driver"),
    path('add_driver', add_driver, name="add_driver"),
    path('delete_driver/<int:driver_id>', delete_driver, name="delete_driver"),
    path('delete_driverDoc/<int:driverDoc_id>', delete_driverDoc, name="delete_driverDoc"),

    path('rentals', rentals, name="rentals"),
    path('add_rental', add_rental, name="add_rental"),
    path('delete_rental/<int:rental_id>', delete_rental, name="delete_rental"),
    path('edit_rental/<int:rental_id>', edit_rental, name="edit_rental"),
    path('view_rental/<int:rental_id>', view_rental, name="view_rental"),
    path('delete_rentalDoc/<int:rentalDoc_id>', delete_rentalDoc, name="delete_rentalDoc"),

    path('print_rental_agreement/<int:rental_id>', print_rental_agreement, name="print_rental_agreement"),
    path('print_rental_sheet/<int:rental_id>', print_rental_sheet, name="print_rental_sheet"),

    path('accounts', accounts, name="accounts"),
    path('add_account/<path:type>', add_account, name="add_account"),
    path('delete_account/<int:account_id>', delete_account, name="delete_account"),

    path('delete_deleted/<int:delete_id>', delete_deleted, name="delete_deleted"),
    path('deletes_view', deletes_view, name="deletes_view"),

    # path('owners', owners, name="owners"),
    # path('view_owner/<int:owner_id>', view_owner, name="view_owner"),
    # path('edit_owner/<int:owner_id>', edit_owner, name="edit_owner"),
    # path('add_owner', add_owner, name="add_owner"),
    # path('delete_owner/<int:owner_id>', delete_owner, name="delete_owner"),
    # path('delete_ownerDoc/<int:ownerDoc_id>', delete_ownerDoc, name="delete_ownerDoc"),


]