from django.urls import include, path
from django.conf.urls.static import static
from . import views
from .views import RegisterView, CustomLoginView, ResetPasswordView, ChangePasswordView

from django.contrib.auth import views as auth_views
from django.conf import settings


from .forms import LoginForm
  
urlpatterns = [
    #path('admin/', admin.site.urls),
    path("select2/", include("django_select2.urls")),
    path("", views.home, name="home"),
    path("sign/",views.sign, name="sign"),
    #path("projects/", views.projects, name="projects"), #matches
    path("profile/", views.profile, name="profile"), #profile
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
     path('projects/', views.projects, name="projects"),

     path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

