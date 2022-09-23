from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.addmovie,name='add_movie'),
    path('update/<int:id>/',views.updatemovie,name='update_movie'),
    path('delete/<int:id>/',views.deletemovie,name='delete_movie'),
]
