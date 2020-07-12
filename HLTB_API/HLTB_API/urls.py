from django.contrib import admin
from django.urls import path,include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hltb/',include('hltbAPI.urls')),
    path('metacritic/',include('metacritic.urls'))
]