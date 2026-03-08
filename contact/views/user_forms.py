from django.shortcuts import render, redirect
from contact.form_con import RegisterForm, Update_forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()

    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
          'form':form
        }
    )

@login_required(login_url='contact:login')
def user_update(request):
#  form = Update_forms(instance=request.user)
 
  if request.method != 'POST':
   if request.user.is_authenticated:
    form = Update_forms(instance=request.user)
    # if request.user.is_authenticated:
    return render(
        request,
        'contact/update_user.html',
        {
          'form':form,
          
        }
    )
    
   return redirect('contact:login')
 
  form = Update_forms(data=request.POST, instance=request.user)
  if not form.is_valid():
    return render(
        request,
        'contact/update_user.html',
        {
          'form':form,
          
        }
    )
 
  form.save()
  return redirect('contact:update')
  

    

def login(request):
     
     form  = AuthenticationForm(request)

     if request.method == 'POST':
         form = AuthenticationForm(request, data=request.POST)
         if form.is_valid():
             user = form.get_user()
             auth.login(request, user)
             messages.success(request, f'Você está logado como {user}.')
             return redirect('contact:indexUser')
         

     return render(
        request,
        'contact/login.html',
        {
          'form':form,
          
        }
    )

@login_required(login_url='contact:login')
def logout(request):
    auth.logout(request)
    return redirect('contact:login')