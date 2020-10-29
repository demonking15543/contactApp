from django.urls import path, include
from .views import signup, activate, profile, profileUpdate
urlpatterns = [

    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('activate/<uidb64>/<token>/', activate, name="activate"),
    path('profile/', profile, name='profile'),
    path('profile_update/', profileUpdate, name='profile-update')
    
]

