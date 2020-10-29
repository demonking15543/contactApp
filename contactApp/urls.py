from django.urls import path
from .views import contact_views, contact_create_view, contact_update_view, contact_delete_view

urlpatterns = [
    
    path('list/', contact_views, name='contact-view'),
    path('new/', contact_create_view, name='new'),
    path('<pk>/update/', contact_update_view, name='contact-update'),
    path('<pk>/delete/', contact_delete_view, name='contact-delete'),

]