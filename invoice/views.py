from django.shortcuts import render, redirect, get_object_or_404
from .models import invoice, company_detail, UserProfile, Product
from .forms import invoiceform, company_detail_form, ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
#view set function for create invoice form.
@login_required(login_url='SignIn')
def InvoiceTemplate(request):
    userId = request.user.id
    invoiceData = UserProfile.objects.get(pk=userId)
    form = invoiceform()
    if request.method=='POST':
        form = invoiceform(request.POST)
        if form.is_valid():
            invoice = form.save()
            invoiceData.invoice_field.add(invoice.id)
            messages.success(request, ('Invoice Created Successfully'))
            
    return render(request, 'form.html', {'form':form})



@login_required(login_url='SignIn')
def InvoiceHomepage(request):
    userId = request.user.id
    invoiceData = UserProfile.objects.get(pk=userId)
    items = invoiceData.invoice_field.all()
        
    return render(request, 'index.html', {'invoiceData':items})




@login_required(login_url='SignIn')
def index(request, id):
    userId = request.user.id
    invoiceData = UserProfile.objects.get(pk=userId)
    item = invoiceData.invoice_field.get(pk=id)
    companydetail = item.company_name
    product = item.product_name.all()
    total_amount = 0
    products = []


    for pro in product:
        total_amount = total_amount + pro.product_price*pro.product_quantity
        newDis = {
            "name":pro.product_name,
            "price":pro.product_price,
            "quantity":pro.product_quantity,
            "total":pro.product_price*pro.product_quantity
        }
        products.append(newDis)

    return render(request, 'one_invoice.html', {'inform':item, 'companydetail':companydetail, 'poduct_name':products, 'total_amount':total_amount})


@login_required(login_url='SignIn')
def companydetailForm(request):
   cmpform = company_detail_form()
   if request.method=='POST':
        cmpform = company_detail_form(request.POST)
        if cmpform.is_valid():
            cmpform.save()
            messages.success(request, ('Company Created Successfully'))
   return render (request, 'companydetail.html', {'cmpform':cmpform})

@login_required(login_url='SignIn')
def productdetail(request):
    pf = ProductForm()
    if request.method =='POST':
        pf = ProductForm(request.POST)
        if pf.is_valid:
            pf.save()
            messages.success(request, ('Product Added Successfully'))
    return render(request, 'product.html', {'pf':pf})


def invoice_edit(request, id):
    userId = request.user.id
    invoiceData = UserProfile.objects.get(pk=userId)
    item = invoiceData.invoice_field.get(pk=id)
    if request.method == 'POST':
        form = invoiceform(request.POST, instance=item)
        if form.is_valid():
            invoice = form.save()
            invoiceData.invoice_field.add(invoice.id)
            messages.success(request, ('Invoice Updated Successfully'))

            return redirect('InvoiceHomepage')
    else:
        form = invoiceform(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'invoice_edit.html', context)

def invoice_delete(request, id):
    userId = request.user.id
    invoiceData = UserProfile.objects.get(pk=userId)
    item = invoiceData.invoice_field.get(pk=id)
    if request.method == 'POST':
        item.delete()
        messages.success(request, ('Invoice Deleted Succesfully'))
        return redirect('InvoiceHomepage')
    context = {
        'item': item
    }
    return render(request, 'delete.html', context)