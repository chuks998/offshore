from urllib import request
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from matplotlib.style import context
from .models import AccountDetail, Transfer
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.db.models import F

# Create your views here.

def login_user(request):
    logout(request)
    username = password = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'login_form.html')


def user(request):
        logged_in_user = request.user
        return logged_in_user




class ProfileView(ListView):
    model = AccountDetail
    template_name = 'dashboard.html'
    context_object_name = 'dashboard'
    queryset = AccountDetail.objects.all()

    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('account_holder'))
    #     context = Transfer.objects.filter(sending_user=user)
    #     return context

    
    def get_context_data(self,  **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['account'] = AccountDetail.objects.all()
        
        context['transfer'] = Transfer.objects.filter(sending_user=self.request.user)
        
        return context

    





def transfer_view(request):
    current_user = request.user
    user_transfer = Transfer.objects.filter(sending_user=current_user)

    return render(request, 'trans_history.html', {'transfer': user_transfer})
        


def transfer(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['reciver_name']
        acct_num = request.POST['account_number']
        amount = request.POST['amount']
        desc = request.POST['desc']
        user = User.objects.get(username=username)
        model = Transfer.objects.create(sending_user=user, reciver_name=name, reciver_account=acct_num, amount=amount, desc=desc)
        if model:
            user_det = AccountDetail.objects.get(account_holder=user)
            user_det.account_balance = F('account_balance') - float(amount)
            user_det.save()
            model.save()
            context = {'bal': user_det.account_balance}

            return redirect('dashboard')

    return render(request, 'transfer_form.html')

def contact(request):
    template = 'contact.html'
    return render(request, template)