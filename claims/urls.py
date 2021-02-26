from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.create_user, name='create'),
    path('login/', auth_views.LoginView.as_view(template_name='claims/authentication.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('file-claim/', views.file_claim, name='file_claim'),
    path('edit-claim/<int:id>/', views.edit_claim, name='edit_claim'),
    path('delete-claim/<int:id>/', views.delete_claim, name='delete_claim'),
]