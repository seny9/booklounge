
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booklounge/', include('booklounge.urls')),
    path('bookclublounge/', include('bookclublounge.urls')),
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),

]
