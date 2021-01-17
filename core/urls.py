from django.contrib import admin
from django.urls import path, include
from core.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="homepage"),
    path('p/', include(('portify.urls', 'portify'), namespace="portify")),
    path('', home, name="homepage/"),
    
]
