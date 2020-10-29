from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import ContactForm
from .models import Contact

# Create your views here.
 
def contact_views(request):
    if request.user.is_authenticated:
        try:
           contacts = request.user.contact_set.all()
        except Exception :
           messages.warning(request, 'You are not registered with us.')
           return redirect('signup')
    else:
        messages.warning(request, 'Login before accessing your contact List.')
        return redirect('%s?next=%s' %(reverse('login'), request.path))

    return render(request, 'contact/view.html', {'contacts': contacts})    

               

def contact_create_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ContactForm(request.POST)           
            if form.is_valid():                   
                form1=form.save(commit=False)  
                form1.user = request.user
                form1.save()            
                messages.success(request, 'contact successfully saved.')                
                return redirect('contact-view')
        else:
            form  = ContactForm(instance=request.user)
    else:
        messages.warning(request, 'signin before saving any contact.')
        return redirect("%s?next=%s" %(reverse('login'), request.path))

          
    return render(request, 'contact/new.html', {'form': form})             







def contact_update_view(request, pk):

    if request.user.is_authenticated:
        try:
            contact = Contact.objects.get(pk=pk)
            if request.user == contact.user:
        
                if request.method == "POST":
                    form = ContactForm(request.POST, instance=contact)
                    if form.is_valid():
                        form1 = form.save(commit=False)
                        form1.save()
                        messages.success( request, 'Contact updated successfully.')
                        return redirect('contact-view')
                else:
                    form = ContactForm(instance=contact)  
            else:
                messages.warning( request, 'This contact does not belong to you.')
                return redirect('contact-view')


            
        except Exception:
            messages.warning(request, "Contact Does not Exist.")
            return redirect('contact-view')
    else:
        messages.warning(request, 'Login before updating  contact')  
        return redirect("%s?next=%s" % (reverse('login'), request.path))
    return render(request, 'contact/contact_update.html', {'form': form})             
     


def contact_delete_view(request, pk):
    if request.user.is_authenticated:
        try:
            contact = Contact.objects.get(pk=pk)
            if request.user == contact.user:
                contact.delete()
                messages.success(request, 'Contact delete successfully')
                return redirect('contact-view')

            else:
                messages.warning(request, "This contact does not belong to you.")
                return redirect('contact-view')



        except Exception:
            messages.warning(request, "Contact Does not exist.")
            return redirect('contact-view')

    else:
        messages.warning(request, 'Login before deleting  contact')  
        return redirect("%s?next=%s" % (reverse('login'), request.path))
              
            


               

