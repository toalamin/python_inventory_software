
from django.contrib import admin
from django.urls import path,include


def home(request):
    return HttpResponse('homepage')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
