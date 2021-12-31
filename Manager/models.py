from django.db import models


class lastSigned(models.Model):
    user_email = models.CharField(max_length=200, blank=False)
    username = models.CharField(max_length=200, blank=False)

class vehicleDocs(models.Model):
    vehicle_id = models.IntegerField(blank=False)
    file_name = models.CharField(max_length=20, blank=False)
    doc = models.FileField(upload_to='vehicleDocs/')

class vehicle(models.Model):
    plate = models.CharField(max_length=20, blank=False, )
    registered_company_name = models.CharField(max_length=100, blank=True, )
    owner_name = models.CharField(max_length=100, blank=True, )
    make = models.CharField(max_length=100, blank=True, )
    model = models.CharField(max_length=100, blank=True, )
    color = models.CharField(max_length=100, blank=True, )
    cylinder_capacity = models.CharField(max_length=100, blank=True, )
    fuel_type = models.CharField(max_length=100, blank=True, )
    year = models.IntegerField(blank=True, )
    mileage = models.IntegerField(blank=True, )
    LOGBOOK_first_date_of_registration = models.DateField(max_length=100, blank=True, )
    mot_expiration_date = models.DateField(max_length=100, blank=True, )
    pco_expiration_date = models.DateField(max_length=100, blank=True, )
    road_tax_expiration_date = models.DateField(max_length=100, blank=True, )
    value = models.IntegerField(blank=True, )
    rent = models.IntegerField(blank=True, )
    STATUS = (
        ('On Rent', 'On Rent'),
        ('Available', 'Available for rent'),
        ('Sold', 'Sold'),
        ('Scrapped', 'Scrapped'),
        ('Damaged', 'Damaged'),
    )
    status = models.CharField(max_length=9, choices=STATUS,  blank=True, )
    notes = models.CharField(max_length=9999, blank=True)



class driver(models.Model):
    email = models.CharField(max_length=100, blank=True, )
    name = models.CharField(max_length=100, blank=True, )
    last_name = models.CharField(max_length=100, blank=True, )
    phone = models.CharField(max_length=30, blank=True, )
    address = models.CharField(max_length=200, blank=True, )
    postcode = models.CharField(max_length=50, blank=True, )
    license_number = models.CharField(max_length=50, blank=True, )
    LN_expiration_date = models.DateField(max_length=100, blank=True, )
    NI = models.CharField(max_length=100, blank=True, )
    birth_date = models.DateField(max_length=100, blank=True, )
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=8, choices=STATUS,  blank=True, )
    notes = models.CharField(max_length=9999, blank=True)

class driverDocs(models.Model):
    driver_id = models.IntegerField(blank=False)
    file_name = models.CharField(max_length=20, blank=False)
    doc = models.FileField(upload_to='driverDocs/')


class rental(models.Model):
    driver_id = models.IntegerField(blank=False, )
    driver_full_name = models.CharField(max_length=200, blank=False, )
    vehicle_id = models.IntegerField(blank=False, )
    vehicle_plate = models.CharField(max_length=20, blank=False, )
    hire_date = models.DateField(max_length=100, blank=False, )
    return_date = models.DateField(max_length=100, blank=False, )
    balance = models.CharField(max_length=99999, blank=False, )
    deposit = models.IntegerField(blank=False, )
    rent = models.IntegerField(blank=False, )
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=8, choices=STATUS,  blank=True, )

class rentalDocs(models.Model):
    rental_id = models.IntegerField(blank=False)
    file_name = models.CharField(max_length=20, blank=False)
    doc = models.FileField(upload_to='rentalDocs/')

class owner_name(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)


class account(models.Model):
    date = models.DateField(blank=False, )
    rental_id = models.IntegerField(blank=False, )
    notes = models.CharField(max_length=100, blank=True, null=True )
    description = models.CharField(max_length=300, blank=False)
    value = models.IntegerField(blank=False, )
    METHODS = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Account Transfer', 'Account Transfer'),
    )
    payment_method = models.CharField(max_length=16, choices=METHODS,  blank=True, )
    TYPES = (
        ('Car Rent', 'Car Rent'),
        ('Expenditure', 'Expenditure'),
        ('PCO', 'PCO'),
        ('Service & Repairs', 'Service & Repairs'),
        ('Other Income', 'Other Income'),
        ('Car Sold', 'Car Sold'),
    )
    type = models.CharField(max_length=17, choices=TYPES,  blank=True, )
    IN_OUT = (
        ('Income', 'Income'),
        ('Outcome', 'Outcome'),
    )
    in_out = models.CharField(max_length=7, choices=IN_OUT,  blank=True, )




class deletes(models.Model):
    user = models.CharField(max_length=300, blank=False)
    description = models.CharField(max_length=300, blank=False)
    link = models.CharField(max_length=300, blank=False)



class permissions(models.Model):
    user = models.CharField(max_length=300, blank=False)
    yesno = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    level1 = models.CharField(max_length=3, choices=yesno,)
    level2 = models.CharField(max_length=3, choices=yesno,)
    level3 = models.CharField(max_length=3, choices=yesno,)
    level4 = models.CharField(max_length=3, choices=yesno,)



class owner(models.Model):
    name = models.CharField(max_length=100, blank=False)
    start = models.DateField(max_length=100, blank=False, )
    end = models.DateField(max_length=100, blank=False, )
    amount_due = models.IntegerField(blank=False, )
    amount_paid = models.IntegerField(blank=False, )
    balance = models.CharField(max_length=99999, blank=False, )

class ownerDocs(models.Model):
    owner_account_id = models.IntegerField(blank=False)
    file_name = models.CharField(max_length=20, blank=False)
    doc = models.FileField(upload_to='ownerDocs/')


