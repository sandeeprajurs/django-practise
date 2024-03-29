from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    title = forms.CharField(required=False)
    # email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if "CFE" not in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     return title
    
    # def clean_email(self, *Args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return email


class RawProductForm(forms.Form):
    title = forms.CharField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    price = forms.DecimalField(initial=199.99)