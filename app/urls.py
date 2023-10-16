from django.urls import include

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import your views from the app

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_contacts/', views.upload_contacts, name='upload_contacts'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
    path('view_video/<int:contact_id>/', views.view_video, name='view_video'),

    
    # Add more URL patterns here
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
