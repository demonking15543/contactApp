from django.urls import path
from .views import AccountListView
urlpatterns = [
    
    
    path('list/', AccountListView.as_view(), name="account_list"),
]
