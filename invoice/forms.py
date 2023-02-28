from django import forms
from .models import invoice, company_detail, Product, UserProfile
from django.contrib.auth.forms import UserCreationForm

class invoiceform(forms.ModelForm):
    class Meta:
        model = invoice
        fields = '__all__'
        widgets = {
            'invoice_number': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'Invoice Number'
                }),
                'date': forms.DateTimeInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                
                }),
            
                'customer_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'Customer Name'
                }),
                'Customer_address': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Customer Address',
                }),
                 'mobile_no': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'Mobile Number',
                }),
                'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'Email',
                }),
                 'company_name': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
              
                }),
                 'product_name': forms.SelectMultiple(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
              
                }),
        }
   

class company_detail_form(forms.ModelForm):
    class Meta:
        model = company_detail
        fields = '__all__'
        widgets = {
            'seller_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'Seller Name'
                }),
                'mobile_no': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'Mobile Number'
                }),
                'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'Email'
                }),
                'seller_address': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'Seller Address'
                }),
                }

class ProductForm(forms.ModelForm):
    class Meta:
        model =Product
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
    
        # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
        # password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None



      