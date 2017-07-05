from django.conf.urls import url
from . import views

app_name = 'user1'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$',views.LoginView.as_view(),name='login_user'),
    url(r'^register/$', views.UserFormView.as_view(),name='register'),
    url(r'^logout/$', views.logoutuser,name='logout_user'),
    url(r'^dashboard$', views.dash_board, name='dash_board')
]
