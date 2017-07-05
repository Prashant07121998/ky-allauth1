
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponse


def index(request):
    return render(request,'user/index.html',)




class UserFormView(View):
    form_class = UserForm
    template_name = 'user/register_form.html'

    def get(self,request):
        if request.user.is_authenticated():
            return redirect('user1:dash_board')
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('user1:dash_board')
        return render(request, self.template_name, {"form": form})





class LoginView(View):
    template_name='user/login123.html'

    def get(self,request):
        if request.user.is_authenticated():
            return redirect('user1:dash_board')
        return render(request, self.template_name,)

    def post(self,request):
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
        except KeyError:
            return render(request, self.template_name, {
                'login_message': 'Fill in all fields', })


        if user is not None:
            if user.is_active:
                auth_login(request, user)
                #return render(request,'user/login_success.html',{'user':user})
                return redirect('user1:dash_board')
        #return render(request, self.template_name, )
        return render(request, self.template_name, {
            'login_message': 'Enter the username and password correctly', })




def logoutuser(request):
    auth_logout(request)
    return redirect('user1:index')





def dash_board(request):
    if request.user.is_authenticated():
        return render(request,'user/dashboard.html',{'user': request.user})
    html = "<h3>You are not logged in</h3><br><p>Click <a href='/user/login/'>here </a> to login</p>"
    return HttpResponse(html)









