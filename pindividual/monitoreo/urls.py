#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include('monitoreo.urls'))
#]

from django.urls import path
from django.urls.resolvers import URLPattern
#from pindividual.monitoreo.views import contacto
from . import views
urlpatterns=[
    path('', views.index, name='monitoreo-index'),
    path('contacto/', views.contacto, name='monitoreo-contacto'), 
    path('recibir/', views.recibir),
    path('clientes/', views.clientes, name= 'monitoreo-clientes'),
    path('ej/', views.ej)
]


