from django.urls import path
from django.contrib.auth.views import (
    LogoutView, 
    PasswordChangeView, 
    PasswordChangeDoneView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetCompleteView, 
    PasswordResetConfirmView
)
from . import views
from django.urls import reverse_lazy

app_name = 'info'

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path("logout/", views.log_out, name='logout'),
    
    path("password_change/", views.UserPasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='info/password_change_done.html'), name='password_change_done'),
    
    path('password_reset/', PasswordResetView.as_view(
        template_name='info/password_reset_form.html',
        email_template_name="info/password_reset_email.html",
        success_url=reverse_lazy("info:password_reset_done")
    ), 
    name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='info/password_reset_done.html'), name='password_reset_done'),
    
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='info/password_reset_confirm.html',
        success_url=reverse_lazy("info:password_reset_complete")
    ), 
    name='password_reset_confirm'),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name='info/password_reset_complete.html'), name='password_reset_complete'),
    
    path("python_intro/", views.python_introduction, name="python_intro"),
    path("error/", views.error, name="error"),
    path("python_syntax/", views.python_syntax, name="python_syntax"), 
    path("create/", views.create, name="create"),
    path("info_from_users/", views.add_info, name="add_info"),
    path("django_info/", views.django_info, name="django_info"),
    path("flask_info/", views.flask_info, name="flask_info"),
    path("pandas_info/", views.pandas_info, name="pandas_info"),
    path("numpy_info/", views.numpy_info, name="numpy_info"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("results/", views.results, name="results"),
    path("vote/", views.vote, name="vote"),
    path("studying/", views.studying, name="studying"),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
]
