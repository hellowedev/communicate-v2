from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login,logout,authenticate
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,Http404

from .forms import UserSignUpForm, UserLoginForm 
from rich.console import Console
console = Console()

def signup_view(request: HttpRequest) :
    if request.method == "POST" :

        sign_up_filled_form = UserSignUpForm(request.POST)
        if sign_up_filled_form.is_valid():
            new_user = sign_up_filled_form.save(commit=False)
            new_user.set_password(sign_up_filled_form.cleaned_data['password1'])

            new_user.save()
            login(request, new_user)
            return redirect('share:index')
        else :
            return redirect('authentication:signup')
    else :
        form = UserSignUpForm()
        return render(request , 'register.html', {'form': form}); 


def login_view(request: HttpRequest) :
        
    console.log(f'Login attempt:\nMETHOD = {request.method}',style="bold blue")

    if request.method == "POST" :
        login_form = UserLoginForm(data = request.POST)
        console.log(login_form.is_valid(),style="bold white")
        if login_form.is_valid():
            console.log('+ validated', style="bold green")
            validated_user = authenticate(request , username = login_form.cleaned_data['username'], password =login_form.cleaned_data['password'])
            console.log(validated_user ,style="bold blue")
            if (validated_user is not None) :
                login(request, validated_user)
                return redirect('share:index' )
            else :
                login_form.add_error(None,'Credentials are not not correct')
                return render(request , 'login.html', {'form': login_form} ); 
    
        else :
            console.log('/ Not validated',style="bold yellow")
            console.log(login_form.errors ,style="bold white")
            return render(request , 'login.html', {'form': login_form} ); 
    else :
        form = UserLoginForm()
        return render(request , 'login.html', {'form': form} ); 
    

def logout_view( request: HttpRequest) :
    console.log('Logout attempt',style="bold blue")
    
    console.log(request.user ,style="bold yellow")
            
    logout(request)
    
    console.log("logout successful" ,style="bold red")
    return render(request , 'logout.html'); 