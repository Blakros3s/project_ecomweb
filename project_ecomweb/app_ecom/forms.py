from django import forms
from .models import Product

class ProductAddForm(forms.ModelForm):
    class Meta:
        # fields = "__all__" #for all fields
        fields = ("title","desc", "price", "category", "quantity", "discount", "cod")
        model = Product