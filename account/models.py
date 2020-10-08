from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
from django.urls import reverse

# Create your models here.

class Account(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True)



    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'


    def __unicode__(self):
        return u'%s' % self.name


    
    def get_absolute_url(self):
        return reverse('account_detail', kwargs={'uuid': self.uuid})  





    def get_update_url(self):
        return reverse('account_update', kwargs={'uuid': self.uuid}) 


    def get_detail_url(self):
        return reverse('account_detail', kwargs={'uuid': self.uuid})                                       





        