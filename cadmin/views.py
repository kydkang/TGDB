from django.shortcuts import render, redirect, get_object_or_404, reverse
from blog.forms import PostForm
from django.contrib import messages
from blog.models import Post, Author, Category, Tag 
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .forms import CustomUserCreationForm
from django_project import helpers
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings



def post_add(request):
    if request.method == "POST":
        f = PostForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Post added.') 
            return redirect('post_add')
    else:
        f = PostForm()
    return render(request, 'cadmin/post_add.html', {'form': f})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        f = PostForm(request.POST, instance=post)     # bound form 
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Post updated.')
            return redirect(reverse('post_update', args=[post.id]))
    # if request is GET, show unbound form to the user, along with data
    else:
        f = PostForm(instance=post)
    return render(request, 'cadmin/post_update.html', {'form': f, 'post':post})

@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'cadmin/admin_page.html')
    
def login(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('/cadmin/')
    else:
        return auth_views.login(request, **kwargs)

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            # send email verification now
            activation_key = helpers.generate_activation_key(username=request.POST['username'])
            subject = "TheGreatDjangoBlog Account Verification"
            message = ('''\nPlease visit the following link to verify your account 
                                    \n\n{0}://{1}/cadmin/activate/account/?key={2}'''
                                .format(request.scheme, request.get_host(), activation_key) )           
            error = False
            try:
                send_mail(subject, message, settings.SERVER_EMAIL, [request.POST['email']])
                messages.add_message(request, messages.INFO, 
                        'Account created! Click on the link sent to your email to activate the account')
            except:
                error = True
                messages.add_message(request, messages.INFO, 
                            'Unable to send email verification. Please try again')
            if not error:
                u = User.objects.create_user(
                        request.POST['username'],
                        request.POST['email'],
                        request.POST['password1'],
                        is_active = 0
                )
                author = Author()
                author.activation_key = activation_key
                author.user = u
                author.save()
            return redirect('register')
    else:
        f = CustomUserCreationForm()
    return render(request, 'cadmin/register.html', {'form': f})


def activate_account(request):
    key = request.GET['key']
    if not key:
        raise Http404()
    r = get_object_or_404(Author, activation_key=key, email_validated=False)
    r.user.is_active = True
    r.user.save()
    r.email_validated = True
    r.save()
    return render(request, 'cadmin/activated.html')

