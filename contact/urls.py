

from django.urls import path
from contact.views import contact_forms, contact_views, user_forms

app_name = 'contact'

urlpatterns = [

    path("", contact_views.index, name='index'),
    path("search/", contact_views.search, name='search'),
  

    # Contact (CRUD)
    path("<int:contact_id>/", contact_views.contact, name='contact'),
    path("contact/create/",  contact_forms.create, name='create'),
    path("<int:contact_id>/update", contact_forms.update, name='update'),
    path("<int:contact_id>/delete", contact_forms.delete, name='delete'),
    

    # User
    path("user/register/", user_forms.register, name='register'),
    path("user/login/", user_forms.login, name='login'),
    path("user/logout/", user_forms.logout, name='logout'),
    path("user/update/", user_forms.user_update, name='update'),
    path("user/index/", contact_views.index_user, name='indexUser'),

]
