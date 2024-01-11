from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404


from django.conf import settings 
from django.conf.urls.static import static 

from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('news/', include('news.urls')),
    # path('', TemplateView.as_view(template_name="news.html"), name='news'),
    # path('news', TemplateView.as_view(template_name="news.html"), name='news'),
    path('about_us', TemplateView.as_view(template_name="about_us.html"), name='about_us'),
    path('gallery', TemplateView.as_view(template_name="gallery.html"), name='gallery'),
    path('contact', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('projects/', include('projects.urls')),
    path('profiles/', include('users.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = views.view_404