from django.urls import path, include
from rest_framework import routers
from denuncia import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'denuncia', views.DenunciaView, 'denuncia')
router.register(r'denunciado', views.DenunciadoView, 'denunciado')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Denuncia API"))

]
