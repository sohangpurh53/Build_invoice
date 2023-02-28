from django.contrib import admin
from .models import invoice, company_detail, Product, UserProfile
# Register your models here.
admin.site.register(invoice)
admin.site.register(company_detail)
admin.site.register(Product)
admin.site.register(UserProfile)
