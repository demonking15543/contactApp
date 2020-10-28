from django.shortcuts import render
from django.views.generic import ListView
from  django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Account
# Create your views here.

class AccountListView(ListView):

    model = Account
    template_name = "accounts/account_list.html"
    context_object_name = 'accounts'


    def get_queryset(self):
        
        
        account_list = Account.objects.filter(owner=self.request.owner) # TODO
        return account_list


    @method_decorator(login_required)
    
    def dispatch(self, request, *args, **kwargs):
        return super(AccountListView, self).dispatch(request, *args, **kwargs)
        
