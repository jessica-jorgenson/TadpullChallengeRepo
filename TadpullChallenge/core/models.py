from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
import urllib.request

CATEGORY_CHOICES = (
    (('1 Person', '1 Person'), ('2 Person', '2 Person'), ('4+ Person', '4+ Person'), ('Accessories', 'Accessories'), ('Backpacks', 'Backpacks'), ('Bags & Duffels', 'Bags & Duffels'), ('Belts', 'Belts'), ('Big & Tall Event', 'Big & Tall Event'), ('Binoculars', 'Binoculars'), ('Black Friday - Cyber Weekend', 'Black Friday - Cyber Weekend'), ('Boots  ', 'Boots  '), ('Business', 'Business'), ('Collections ', 'Collections '), ('Coolers', 'Coolers'), ('Electronics', 'Electronics'), ('Essentials', 'Essentials'), ("Father's Day", "Father's Day"), ('Food', 'Food'), ('Game Calls', 'Game Calls'), ('Gifts', 'Gifts'), ('Gifts under $100', 'Gifts under $100'), ('Gifts under $50', 'Gifts under $50'), ('Gloves', 'Gloves'), ('Hammocks', 'Hammocks'), ('Hats', 'Hats'), ('Hydration', 'Hydration'), ('Jackets & Vests', 'Jackets & Vests'), ('Knives & Tools', 'Knives & Tools'), ('Lighting', 'Lighting'), ('Logo Apparel', 'Logo Apparel'), ('Maps', 'Maps'), ('Medical & Survival', 'Medical & Survival'), ('Memorial Day Sale', 'Memorial Day Sale'),
     ("Men's", "Men's"), ('Mountain Boots', 'Mountain Boots'), ('Mystery Ranch Sale', 'Mystery Ranch Sale'), ('Other', 'Other'), ('Outerwear', 'Outerwear'), ('Pac Boots', 'Pac Boots'), ('Packs', 'Packs'), ('Pants & Bottoms', 'Pants & Bottoms'), ('Pots & Pans', 'Pots & Pans'), ('Promo Code Apply', 'Promo Code Apply'), ('Rangefinders', 'Rangefinders'), ('Rifle', 'Rifle'), ('Rifle Scopes', 'Rifle Scopes'), ('Sale', 'Sale'), ('Shirts & Tops', 'Shirts & Tops'), ('Shoes', 'Shoes'), ('Sleeping Bags', 'Sleeping Bags'), ('Sleeping Pads', 'Sleeping Pads'), ('Slippers', 'Slippers'), ('Socks', 'Socks'), ('Spotting Scopes', 'Spotting Scopes'), ('Stoves & Burners', 'Stoves & Burners'), ('Sunglasses', 'Sunglasses'), ('Tableware', 'Tableware'), ('Uncategorized', 'Uncategorized'), ('Uncategorized Heartland Retail Items', 'Uncategorized Heartland Retail Items'), ('Uncategorized Springboard Items', 'Uncategorized Springboard Items'), ('Various', 'Various'), ('Walking', 'Walking'), ('Wallets', 'Wallets'), ("Women's", "Women's"))
)

LABEL_CHOICES = (
    ('IND', 'In Demand'),
)


class Item(models.Model):

    imageurl = models.URLField()
    name = models.CharField(max_length=100)

    quantityAvailable = models.IntegerField(default=0)
    quantitySold = models.IntegerField(default=0)
    price = models.FloatField()
    slug = models.SlugField(default="")
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def url_is_alive(self):
        request = urllib.request.Request(self.imageurl)
        request.get_method = lambda: 'HEAD'

        try:
            urllib.request.urlopen(request)
        except urllib.request.HTTPError:
            self.imageurl = "../../static/img/unavailable.jpg"
        return self.imageurl

    def __str__(self):
        return self.name

    def get_label(self):
        if self.label == "In Demand":
            return "warning"

    def format_quantity(self):
        if self.label == "In Demand":
            return "low-quantities"
        return "quantities"

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def formatted_price(self):
        if "." in str(self.price):
            digits = len(str(self.price).split('.')[1])
            if digits == 1:
                return str(self.price) + "0"
        return str(self.price)
