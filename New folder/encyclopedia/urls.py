from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("newpage/", views.newpage, name="newpage"),
    path("save/",views.save,name="save"),
    path("search/",views.search, name="search"),
    path("editpage/<str:title>",views.editpage,name="editpage"),
    path("editted/<str:title>",views.edit,name="edit"),
    path("random/",views.randompage,name="random")
]

