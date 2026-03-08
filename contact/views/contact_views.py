
from django.shortcuts import  get_object_or_404, render, redirect
from django.db.models import Q
from contact.models import Contact
from django.http import Http404
from django.core.paginator import Paginator


def search(request):
   search_value = request.GET.get('q','').strip()
   
   if search_value=='':
    return redirect('contact:index')
   
   
   search = Contact.objects\
      .filter(show=True)\
      .order_by('-id')\
      .filter(
         Q(first_name__icontains = search_value)|
         Q(id__icontains = search_value)|
         Q(last_name__icontains = search_value)
         
         
         )
      
   
   
   context = {
      'page_obj': search
   }

   return render(
      request,
      'contact/index.html',
      context

    )


def index_user(request):
    contacts = Contact.objects \
        .filter(show=True,owner=request.user )\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index_user.html',
        context
    )


def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
   #contacts_single = Contact.objects.filter(pk=contact_id).first() 
   single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

   
   context = {
      'contacts': single_contact
   }

   return render(
      request,
      'contact/contact.html',
      context

    )
