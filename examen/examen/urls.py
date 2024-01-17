from django.contrib import admin
from django.urls import path, include
#from countries.views import index




urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', index('countries.urls')),
    path('country/', include('countries.urls')),
    path('city/', include('countries.urls'))
]

