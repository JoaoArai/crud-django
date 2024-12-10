"""
URL configuration for ung project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import ProdutosListView,ProdutosCreateView,ProdutosUpdateView, ProdutosDeleteView, ProdutosDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path ('' ,ProdutosListView.as_view(), name='produto-list'),
    path ('produtos/add/' ,ProdutosCreateView.as_view(), name='produto-create'),
    path ('produtos/<int:pk>/update/', ProdutosUpdateView.as_view(), name='produto-update'),
    path ('produtos/<int:pk>/delete/', ProdutosDeleteView.as_view(), name='produto-delete'),
    path ('produtos/<int:pk>/', ProdutosDetailView.as_view(), name='produto-detail'),  
]