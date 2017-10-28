from django.conf.urls import url
from . import views

app_name='main'
urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^register/$',views.UserFormView.as_view(), name='register'),
	url(r'^login/$',views.UserLoginView.as_view(), name='login'),
	url(r'^home/$',views.home, name='home'),
	]