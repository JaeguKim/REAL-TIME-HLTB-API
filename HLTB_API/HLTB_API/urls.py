from django.contrib import admin
from django.urls import path
from hltbAPI.views import ListCurrencyView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListCurrencyView.as_view())
]