
from django.urls import path


from . import views
app_name='myworks'
urlpatterns = [

    path('',views.all_myworks,name='all_myworks'),
    path('<int:myworks_id>/',views.detail,name='detail'),


]
