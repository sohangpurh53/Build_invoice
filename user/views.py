from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from invoice.forms import CustomUserCreationForm

# Create your views here.

#user login code here
def SignIn(request):
       if request.method == 'POST':
              username = request.POST['username']
              password = request.POST['password']
              user = authenticate(request, username=username, password=password)
              if user is not None:
               login(request, user)
               messages.success(request, ('Login Successfull: ' +username.capitalize()))
              # Redirect to a success page.
               return redirect('InvoiceHomepage')
              
              else:
                     messages.success(request, ('There is an Error while Logging in..'))
                     return redirect('SignIn')
              # Return an 'invalid login' error message.
       else:
        return render(request, 'User_Authenticate/signin.html')

#user logout code 
def SignOut(request):
       logout(request)
       messages.success(request, ('Logout Succesfully'))
       return redirect('InvoiceHomepage')

#user registration code
def SignUp(request):
       if request.method =='POST':
              form = CustomUserCreationForm(request.POST)
              if form.is_valid():
                     form.save()
                     username = form.cleaned_data['username']
                     password = form.cleaned_data['password1']
                     user = authenticate(username=username, password=password)
                     login(request, user)
                     messages.success(request, ('User registration Successfull..'))
                     return redirect('InvoiceHomepage')
       else:
              form = CustomUserCreationForm()

       return render(request, 'User_Authenticate/signup.html', {'form':form})