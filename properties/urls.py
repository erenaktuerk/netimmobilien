from django.urls import path
from . import views

app_name = 'properties'
# the url father node is 'immobilien/'
urlpatterns = [
    # <int:id>
    path('detail/<int:id>', views.property_detail, name='property_detail'),
    path('anbieten/', views.immoAnbieten, name='immobilieanbieten'),
    path('suchauftrag/', views.searchOrder, name="searchorder"),
    path('immobilienverrentung/', views.immobilienverrentung,
         name="immobilienverrentung"),
    path('immobilienpflege/', views.immobilienpflege, name="immobilienpflege"),
    path('auslandsimmobilien/', views.immoausland, name="immoausland"),

    #path('properties', views.properties, name='properties2'),

    path('', views.properties, name='properties'),

]
