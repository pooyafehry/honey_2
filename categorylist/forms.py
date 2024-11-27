# categorylist/forms.py
from django import forms
from .models import Category, CartItem, Comment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class CartAddForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
