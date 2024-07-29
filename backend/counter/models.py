from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt


class MarketingCounter(models.Model):
    """
    Model representing a marketing counter. (All data is encrypted in the database)

    Attributes:
        owner (ForeignKey): The user who owns the marketing counter.
        phone (CharField): The encrypted phone number of the customer.
        name (CharField): The encrypted name of the customer.
        customerBin (CharField): The encrypted customer bin.
        email (CharField): The encrypted email address of the customer.
        subject (TextField): The encrypted subject.
        city (CharField): The encrypted city of the customer.
        url (TextField): The encrypted URL.
        utmSource (TextField): The encrypted UTM source.
        utmMedium (TextField): The encrypted UTM medium.
        utmTerm (TextField): The encrypted UTM term.
        utmContent (TextField): The encrypted UTM content.
        utmCampaign (TextField): The encrypted UTM campaign.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = encrypt(models.CharField(max_length=255, null=True, blank=True))
    name = encrypt(models.CharField(max_length=255, null=True, blank=True))
    customerBin = encrypt(models.CharField(max_length=255, null=True, blank=True))
    email = encrypt(models.CharField(max_length=255, null=True, blank=True))
    subject = encrypt(models.TextField(null=True, blank=True))
    city = encrypt(models.CharField(max_length=255, null=True, blank=True))
    url = encrypt(models.TextField(null=True, blank=True))
    utmSource = encrypt(models.TextField(null=True, blank=True))
    utmMedium = encrypt(models.TextField(null=True, blank=True))
    utmTerm = encrypt(models.TextField(null=True, blank=True))
    utmContent = encrypt(models.TextField(null=True, blank=True))
    utmCampaign = encrypt(models.TextField(null=True, blank=True))
    