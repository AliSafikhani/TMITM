"""
URL configuration for transformer_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from transformers import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('transformer_spec', views.transformer_spec, name='transformer_spec'),
    path('add_transformer', views.add_transformer, name='add_transformers'),
    path('add', views.add, name='add'),
    path('test', views.test, name='test'),
    path('search', views.search, name='search'),
    path('show', views.show, name='show'),
    path('edit/<int:id>/', views.edit_transformer, name='edit_transformer'),
    path('delete/<int:id>/', views.delete_transformer, name='delete_transformer'),
    path('test/dga', views.dga, name='dga'),
    path('test/dga/dga_resaults', views.dga_resaults, name='dga_resaults'),
    path('test/dga/add_dga_test_resaults', views.add_dga_test_resaults, name='add_dga_test_resaults'),
    path('test/dga/add_dga_test_resaults/dga_gas_adding/', views.dga_gas_adding, name='dga_gas_adding'),
    path('test/dga/add_dga_test_resaults/dga_gas_adding/dga_gas_adding_dga', views.dga_gas_adding_dga, name='dga_gas_adding_dga'),
    path('test/dga/doal', views.doal, name='doal'),
    path('test/dga/doal/doal_resault', views.doal_resault, name='doal_resault'),
    path('test/fra', views.fra, name='fra'),
    path('test/resistance', views.resistance, name='resistance'),
    path('test/tan_delta', views.tan_delta, name='tan_delta'),
    path('upload/', views.upload_file, name='upload_file'),
    path('plot/', views.plot_data, name='plot_data'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
