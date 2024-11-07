
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('insert',views.insertdata,name="insertdata"),
    path('update/<id>',views.updateData,name="updateData"),
    path('delete/<id>',views.deleteData,name="deletedata"),
]