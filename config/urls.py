from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# 🔥 ADD THESE
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('users/', include('users.urls')),
    path('soil/', include('soil.urls')),
    path('map/', include('map_locator.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('feedback/', include('feedback.urls')),

    path('how-to-use/', TemplateView.as_view(template_name='how_to_use.html'), name='how_to_use'),
]

# 🔥 THIS LINE FIXES IMAGE DISPLAY
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)