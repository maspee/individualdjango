#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include('monitoreo.urls'))
#]
from django.conf import settings
#from django.conf.urls.statics import static
from django.urls import path
from django.urls.resolvers import URLPattern
#from pindividual.monitoreo.views import contacto
from . import views
urlpatterns=[
    path('', views.index, name='monitoreo-index'),
    path('contacto/', views.contacto, name='monitoreo-contacto'), 
    path('recibir/', views.recibir),
    path('clientes/', views.clientes, name= 'monitoreo-clientes'),
    path('recibirReclamo', views.reclamo),
    path('reclamov2', views.reclamo2),
    path('cliente2', views.clientes2, name='monitoreo-cliente2'),
    path('ej/', views.ej)
]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
