from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('dictionary/<int:pk>/detail',
         views.dictionary_detail, name='dictionary_detail'),
    path('dictionary/create', views.create_dictionary, name='create_dictionary'),
    path('dictionary/category/create', views.create_dictionary_category,
         name='create_dictionary_category'),

    path('dictionary/<int:dictionary_pk>/term/create',
         views.create_term, name='create_term'),
    path('dictionary/<int:dictionary_pk>/term/category/create', views.create_term_category,
         name='create_term_category'),
]
