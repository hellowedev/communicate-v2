from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required 

from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,Http404

from .forms import ShareForm

from .models import Share

# Create your views here.

# List all shares now .
def index(request: HttpRequest) :
    shares_list = shares_list_complete()
    return render(request , 'index.html', {'shares': shares_list})

@login_required
def share_delete(request: HttpRequest , share_id) :

    share_initial = get_object_or_404(Share , pk = share_id, user = request.user)

    if request.method == 'POST' :
        share_initial.delete( )
        return redirect('share:index')
    else :
        share_new_form = ShareForm(instance=share_initial)
        return render(request , 'share_delete_confirmations.html' , { 'form' : share_new_form})

@login_required
def share_edit(request: HttpRequest , share_id) :
    share_initial = get_object_or_404(Share , pk = share_id, user = request.user)

    if request.method == 'POST' :
        share_filled_form = ShareForm(request.POST, request.FILES, instance=share_initial)
        if share_filled_form.is_valid() :
            share_form = share_filled_form.save(commit=False)
            user = request.user 
            share_form.user = user 

            share_form.save()
            return redirect('share:index')
        else :
            return redirect('share:index')
    else :
        share_new_form = ShareForm(instance=share_initial)
        return render(request , 'create_share.html' , {'form' : share_new_form})

@login_required 
def share_create(request: HttpRequest) :
    if request.method == 'POST' :
        share_filled_form = ShareForm(request.POST, request.FILES)
        if share_filled_form.is_valid() :
            share_form = share_filled_form.save(commit=False)
            user = request.user 
            share_form.user = user 

            share_form.save()
            return redirect('share:index')
        else :
            return redirect('share:index')
    else :
        share_new_form = ShareForm()
        return render(request , 'create_share.html' , {'form' : share_new_form})
    
def shares_list_complete() :
    shares_list = Share.objects.all().order_by('-created_at')
    return shares_list ;