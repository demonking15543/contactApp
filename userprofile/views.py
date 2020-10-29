from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import SignupForm, UserEdit, ProfileEdit
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/email_template.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})




    

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(
            request,
            'Thank you for your email confirmation. Now you can login your account.',
            fail_silently=True)
        
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')




def profile(request):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            return render(request, 'profile/view.html', {'profile': profile})
        except Exception:
            messages.success(request, "You are not registered with us.")
            return redirect('signup')
    else:
        messages.warning(request, 'Login before viewing your profile.') 
        return redirect(('%s?next=%s' % (reverse('login'), request.path))) 


@login_required(login_url='login')
def profileUpdate(request):

    if request.method == "POST":
        form1 = UserEdit(request.POST, instance=request.user)
        form2 = ProfileEdit(request.POST, instance=request.user.profile)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, 'Your profile successfully updated.')
            return redirect('profile')

    else:
        form1 = UserEdit(instance=request.user)
        form2 = ProfileEdit(instance=request.user.profile)

    context = {'form1': form1, 'form2': form2}
    return render(request, 'profile/update_form.html', context)    
        
            

