from django.contrib import admin
from .models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('user', 'name', 'contact', 'email', 'location', 'created_on', 'update_on')
    search_fields = ('name', 'contact', 'location')
    
    