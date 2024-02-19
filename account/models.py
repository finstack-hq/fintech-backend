from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField
# from userauths.models import User
from userauths.models import CustomUser
from django.db.models.signals import post_save

ACCOUNT_STATUS = (
    ("active", "Active"),
    ("pending", "Pending"),
    ("in-active", "In-active")
)

MARITAL_STATUS = (
    ("married", "Married"),
    ("single", "Single"),
    ("other", "Other")
)

GENDER = (
    ("male", "Male"),
    ("female", "Female"),
    ("other", "Other")
)

TRANSACTION_TYPE = (
   ("Bank Transfer", "Bank Transfer"),
   ("Cash Deposit", "Cash Deposit"),
   ("Mobile Money", "Mobile Money"),
   ("Other", "Other")
)

TRANSACTION_ORIGIN = (
   ("Bank", "Bank"),
   ("Wallet", "Wallet"),
   ("Momo Name", "Momo Name"),
   ("Other", "Other")
)

CURRENCY_TO  = (
   ("European Euro", "European Euro"),
   ("British pound", "British pound"),
   ("United States dollar", "United States dollar"),
)

CURRENCY_FROM = (
   ("European Euro", "European Euro"),
   ("British pound", "British pound"),
   ("United States dollar", "United States dollar"),
)


IDENTITY_TYPE = (
    ("national_id_card", "National ID Card"),
    ("drivers_licence", "Drives Licence"),
    ("international_passport", "International Passport"),
    ("NIN", "NIN"),
    ("BVN", "BVN")
)


def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)

class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) #123 345 789 102
    account_number = ShortUUIDField(unique=True,length=10, max_length=25, prefix="217", alphabet="1234567890") #2175893745837
    account_id = ShortUUIDField(unique=True,length=7, max_length=25, prefix="DEX", alphabet="1234567890") #2175893745837
    pin_number = ShortUUIDField(unique=True,length=4, max_length=7, alphabet="1234567890") #2737
    red_code = ShortUUIDField(unique=True,length=10, max_length=20, alphabet="abcdefgh1234567890") #2737
    account_status = models.CharField(max_length=100, choices=ACCOUNT_STATUS, default="in-active")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="recommended_by")
    review = models.CharField(max_length=100, null=True, blank=True, default="Review")
    
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.user}"

class KYC(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    account =  models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="kyc", default="default.jpg")
    # image = models.ImageField(upload_to="static/images/", null=True, blank=True)
    marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40)
    gender = models.CharField(choices=GENDER, max_length=40)
    identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140)
    identity_image = models.ImageField(upload_to="kyc", null=True, blank=True)
    date_of_birth = models.DateTimeField(auto_now_add=False)
    signature = models.ImageField(upload_to="kyc")

    # Address
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # Contact Detail
    mobile = models.CharField(max_length=1000)
    fax = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user}"    

    
    class Meta:
        ordering = ['-date']

class SENDUSER(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    account =  models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=1000, null=True, blank=True)
    # image = models.ImageField(upload_to="kyc", default="default.jpg")
    # marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40, blank=True, null=True)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=40, null=True, blank=True)
    # gender = models.CharField(choices=GENDER, max_length=40, blank=True, null=True)
    # transaction_origin = models.CharField(choices=TRANSACTION_ORIGIN, max_length=40, null=True, blank=True)
    transaction_origin = models.CharField(max_length=1000, null=True, blank=True)
    # identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140, blank=True, null=True)
    # identity_image = models.ImageField(upload_to="sent", null=True, blank=True)
    # date_of_birth = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    # signature = models.ImageField(upload_to="sent", blank=True, null=True)

    # Address
    other = models.CharField(max_length=100, blank=True, null=True)
    # state = models.CharField(max_length=100, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)

    # Contact Detail
    mobile = models.CharField(max_length=1000, null=True, blank=True)
    account_number = models.CharField(max_length=1000, null=True, blank=True)
    # fax = models.CharField(max_length=1000, blank=True, null=True)
    # date = models.DateTimeField(auto_now_add=True, blank=True, null=True )


    def __str__(self):
        return f"{self.user}"    

    
    class Meta:
        ordering = ['-full_name']

class RECEIVEUSER(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    account =  models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=1000)
    # image = models.ImageField(upload_to="kyc", default="default.jpg")
    # marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40, blank=True, null=True)
    # gender = models.CharField(choices=GENDER, max_length=40, blank=True, null=True)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=40, null=True, blank=True)
    # transaction_origin = models.CharField(choices=TRANSACTION_ORIGIN, max_length=40, null=True, blank=True)
    transaction_origin = models.CharField(max_length=1000, null=True, blank=True)
    # identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140, blank=True, null=True)
    identity_image = models.ImageField(upload_to="receive", null=True, blank=True)
    account_number = models.CharField(max_length=1000, null=True, blank=True)
    other = models.CharField(max_length=100, blank=True, null=True)
    # date_of_birth = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    # signature = models.ImageField(upload_to="receive", blank=True, null=True)

    # Address
    # country = models.CharField(max_length=100, blank=True, null=True)
    # state = models.CharField(max_length=100, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)

    # Contact Detail
    # mobile = models.CharField(max_length=1000, blank=True, null=True)
    # fax = models.CharField(max_length=1000, blank=True, null=True)
    # date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f"{self.user}"    

    
    class Meta:
        ordering = ['-full_name']

class CURRENCY_CONVERTOR(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user =  models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    account =  models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=1000, null=True, blank=True)

    # result = models.CharField(max_length=1000)
    amount = models.CharField(max_length=1000, null=True, blank=True)
    # currency_to = models.CharField(max_length=1000)
    # currency_from = models.CharField(max_length=1000)
    currency_from = models.CharField(choices=CURRENCY_FROM, max_length=40, null=True, blank=True)
    currency_to = models.CharField(choices=CURRENCY_TO, max_length=40, null=True, blank=True)
    # currency_data = models.CharField(max_length=1000)
    # image = models.ImageField(upload_to="kyc", default="default.jpg")
    # marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40, blank=True, null=True)
    # gender = models.CharField(choices=GENDER, max_length=40, blank=True, null=True)
    # transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=40, null=True, blank=True)
    # transaction_origin = models.CharField(choices=TRANSACTION_ORIGIN, max_length=40, null=True, blank=True)
    # identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140, blank=True, null=True)
    # identity_image = models.ImageField(upload_to="receive", null=True, blank=True)
    # account_number = models.CharField(max_length=1000, null=True, blank=True)
    # other = models.CharField(max_length=100, blank=True, null=True)
    # date_of_birth = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    # signature = models.ImageField(upload_to="receive", blank=True, null=True)

    # Address
    # country = models.CharField(max_length=100, blank=True, null=True)
    # state = models.CharField(max_length=100, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)

    # Contact Detail
    # mobile = models.CharField(max_length=1000, blank=True, null=True)
    # fax = models.CharField(max_length=1000, blank=True, null=True)
    # date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return f"{self.user}"    

    
    class Meta:
        ordering = ['-full_name']


def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

def save_account(sender, instance,**kwargs):
    instance.account.save()

post_save.connect(create_account, sender=CustomUser)
post_save.connect(save_account, sender=CustomUser)




