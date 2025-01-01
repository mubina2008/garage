from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,\
    PasswordChangeView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
from .views import dashboard_view, user_register,edit_user
urlpatterns = [
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('profile/', dashboard_view, name='user_profile'),
    path('password-change/',PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/',PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/<vidb64>/<token>',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset/complete/',PasswordResetCompleteView,name='user_register'),
    path('signup/', user_register, name='user_register'),
    path('profile/edit/', edit_user, name='profile_edit')

]