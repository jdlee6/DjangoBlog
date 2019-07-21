from django.shortcuts import render, redirect
from django.contrib import messages
# import new form with email
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        # change form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else: 
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

''' 
different types of messages:

message.debug
message.info
message.success
message.warning
message.error
'''
