from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View, FormView
from .forms import UserForm, UserLoginForm

def index(request):
	return render(request,'main/index.html')


def home(request):
	return render(request,'main/home.html')

class UserLoginView(FormView):
	form_class = UserLoginForm
	template_name = 'main/login.html'
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form': form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			#returns User objects if credentials are correct
			user = authenticate(username=username, password=password)
			
			
			if user is not None:
				if user.is_active:
					login(request,user)
					#request.user.username
					return redirect('main:home')
				
		return render(request,self.template_name,{'form': form})

class UserFormView(View):
	form_class = UserForm
	template_name = 'main/register.html'
	
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form': form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			user = form.save(commit=False)
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.setpassword(password)
			user.save()
			
			#returns User objects if credentials are correct
			user = authenticate(username=username, password=password)
			
			if user is not None:
				if user.is_active:
					login(request,user)
					#request.user.username
					return redirect('main:index')
				
		return render(request,self.template_name,{'form': form})