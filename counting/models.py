from django.conf import settings
from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.fields.json import JSONField


class family(models.Model):
    family_name = models.CharField(max_length=50)


class parishoners(models.Model):
    full_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    family = models.ForeignKey(family, on_delete=models.CASCADE, null=True)


class parishoner_state(models.Model):
    full_state_name = models.CharField(max_length=100)
    state_abbr = models.CharField(max_length=10)


class parishoner_address(models.Model):
    parishoner = models.ForeignKey(parishoners, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50)
    state = models.ForeignKey(parishoner_state, on_delete=models.CASCADE)
    zip = models.IntegerField()


class contact_type(models.Model):
    contact_name = models.CharField(max_length=50)


class parishoner_contact(models.Model):
    parishoner = models.ForeignKey(parishoners, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(contact_type, on_delete=models.CASCADE)
    contact_data = models.CharField(max_length=100)


class payment_type(models.Model):
    payment_type_name = models.CharField(max_length=50)


class donation_category(models.Model):
    category_name = models.CharField(max_length=50)
    category_qb_account = models.CharField(max_length=200,null=True)

class donation_category_custom(models.Model):
    category_name = models.CharField(max_length=255)
    category_type = models.ForeignKey(donation_category, on_delete=models.CASCADE)

class count_type(models.Model):
    count_type_name = models.CharField(max_length=50)


class count(models.Model):
    count_date = models.DateField()
    count_type = models.ForeignKey(count_type, on_delete=models.CASCADE)
    user_id = models.IntegerField()


class donation_detail(models.Model):
    check_number = models.CharField(max_length=50, null=True)
    meta_data = models.TextField(null=True)


class named_donations(models.Model):
    count = models.ForeignKey(count, on_delete=models.CASCADE)
    parishoner = models.ForeignKey(parishoners, on_delete=models.CASCADE)
    category = models.ForeignKey(donation_category, on_delete=models.CASCADE)
    donation_date = models.DateField()
    payment_type = models.ForeignKey(payment_type, on_delete=models.CASCADE)
    donation_detail_id = models.ForeignKey(donation_detail, on_delete=models.CASCADE, null=True)
    donation_total = models.DecimalField(max_digits=8, decimal_places=2)
    custom_category = models.ForeignKey(donation_category_custom, on_delete=models.CASCADE, null=True)


class donation_note(models.Model):
    donation_note = models.TextField()
    count = models.ForeignKey(count, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(donation_category, on_delete=models.CASCADE, null=True)
    custom_category = models.ForeignKey(donation_category_custom, on_delete=models.CASCADE, null=True)


class unnamed_donations(models.Model):
    count = models.ForeignKey(count, on_delete=models.CASCADE)
    category = models.ForeignKey(donation_category, on_delete=models.CASCADE)
    donation_date = models.DateField()
    payment_type = models.ForeignKey(payment_type, on_delete=models.CASCADE)
    one_count = models.IntegerField(default=0)
    two_count = models.IntegerField(default=0)
    five_count = models.IntegerField(default=0)
    ten_count = models.IntegerField(default=0)
    twenty_count = models.IntegerField(default=0)
    fifty_count = models.IntegerField(default=0)
    hundred_count = models.IntegerField(default=0)
    donation_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    donation_note = models.ForeignKey(donation_note, on_delete=models.CASCADE, default=1)
    custom_category = models.ForeignKey(donation_category_custom, on_delete=models.CASCADE, null=True)

class counter(models.Model):
    full_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    user_id = models.IntegerField()
    text_reminders = models.BooleanField()
    email_reminders = models.BooleanField()


class counter_schedule(models.Model):
    counter = models.ForeignKey(counter, on_delete=models.CASCADE)
    scheduled_date = models.DateField()

class autosave(models.Model):
    count = models.ForeignKey(count, on_delete=models.CASCADE)
    data = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)




#     groups



















# class email_queue(models.Model):







# Things I need
#counter_schedule
#email queue
#text_queue
#qb_sync_data


    # price = models.DecimalField(max_digits=5, decimal_places=2)
    # item_type_id = models.ForeignKey(ProductTypes, on_delete=models.CASCADE, db_column="item_type_id")
#
#
# class Order_Type(models.Model):
#     type = models.CharField(max_length=50)
#
#
# class Locations(models.Model):
#     location_name = models.CharField(max_length=50)
#     location_address = models.CharField(max_length=50)
#     location_city = models.CharField(max_length=50)
#     location_state = models.CharField(max_length=25)
#     location_zip = models.IntegerField()
#     location_image = models.TextField(null=True)
#
#
# class Customer(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
#     delivery_type = models.IntegerField(null=True)
#     first_name = models.CharField(max_length=50, null=True)
#     last_name = models.CharField(max_length=50, null=True)
#     address = models.CharField(max_length=100, null=True)
#     city = models.CharField(max_length=50, null=True)
#     state = models.CharField(max_length=25, null=True)
#     zip_code = models.IntegerField(null=True)
#     email = models.CharField(max_length=50, null=True)
#     phone_number = models.BigIntegerField(null=True)
#     visitor_id = models.BigIntegerField(null=True)
#
#
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
#     order_type = models.ForeignKey(Order_Type, on_delete=models.CASCADE, null=True)
#     location = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, related_name="related_location")
#     subtotal = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#     delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#     tax = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#     grand_total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#     order_completed = models.BooleanField(null=True)
#
#
# class Cart(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="related_order")
#     item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="related_item")
#     quantity = models.DecimalField(max_digits=4, decimal_places=0)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     total_price = models.DecimalField(max_digits=6, decimal_places=2)
#     product_name = models.CharField(max_length=100, null=True)
#     product_picture = models.TextField(default='Does Not Exist')
#
#
# class Careers(models.Model):
#     position = models.CharField(max_length=50, null=True)
#     from_email = models.CharField(max_length=50, null=True)
#     resume = models.CharField(max_length=3000, null=True)
#     first_name = models.CharField(max_length=50, null=True)
#     last_name = models.CharField(max_length=50, null=True)
#     phone_number = models.BigIntegerField(null=True)
#
#
# class Payment_Types(models.Model):
#     payment_method = models.CharField(max_length=20, null=True)
#
#
# class Payments(models.Model):
#     customer_number = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name="related_customer")
#     order_number = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="order_number")
#     payment_type = models.ForeignKey(Payment_Types, on_delete=models.CASCADE, null=True, related_name="related_payment_type")
#     payment_total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
#
#
# class Credit_Card_Types(models.Model):
#     card_type = models.CharField(max_length=50, null=True)
#
#
# class Payment_Details(models.Model):
#     billing_full_name = models.CharField(max_length=50, null=True)
#     billing_email = models.CharField(max_length=50, null=True)
#     billing_address = models.CharField(max_length=100, null=True)
#     billing_city = models.CharField(max_length=50, null=True)
#     billing_state = models.CharField(max_length=25, null=True)
#     billing_zip = models.IntegerField(null=True)
#     payment = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True, related_name="related_payment")
#     customer_name = models.CharField(max_length=100, null=True)
#     billing_name = models.CharField(max_length=100, null=True)
#     credit_card_number = models.BigIntegerField(null=True)
#     expiration_month = models.CharField(max_length=50, null=True)
#     expiration_year = models.CharField(max_length=50, null=True)
#     security_code = models.IntegerField(null=True)
#     type = models.ForeignKey(Credit_Card_Types, on_delete=models.CASCADE, null=True, related_name="related_card_type")
#
#
# class Promo_Code_Payment(models.Model):
#     promo_code_used = models.IntegerField(null=True)
#     payment = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True, related_name="promo_payment")
#
#
# class Cash_Payment(models.Model):
#     payment = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True, related_name="cash_payment")
