from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('dictionary/<slug:slug>', views.get_terms_of_dictionary,
         name='get_terms_of_dictionary'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

]
