from django.urls import path
from . import views

app_name = "fitnessapp"

urlpatterns = [
    path("blogs/add", views.add_blog, name="Add blog"),
    path("blogs/all", views.list_blogs, name="list blogs"),
    path("blogs/update/<blog_id>", views.update_blog, name="update_blog"),
    path("blogs/delete/<blog_id>", views.delete_blog, name="delete_blog"),
    path("comment/add",views.add_comment, name="Add comment"),
    path("comment/all",views.list_comment,name= "list comments"),
    path("comment/update/<comment_id>",views.update_comment, name="update_comment"),
    path("comment/delete/<comment_id>", views.delete_comment,name= "delete_comment"),

]