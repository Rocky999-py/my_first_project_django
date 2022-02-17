from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('addmusician/',views.add_musician,name="musician"),
    path('list/<int:idi>/',views.list,name="list"),
    path('new/<int:idi>/',views.new,name="new"),
    path('post/',views.post,name="post"),
    path('addartist/',views.addartist,name="artist"),
    path('editmusician/<int:idik>/',views.edit,name="edit"),
    path('update/',views.update,name="update"),
     path('update2/<int:idki>/',views.update2,name="update2"),
     path('delete/<int:aid>/',views.delete,name="delete")
]
