from django.urls import path
from . import views

app_name = "fitnessapp"

urlpatterns = [
    path("blogs/add", views.add_blog, name="Add blog"),
    path("blogs/all", views.list_blogs, name="list blogs"),
    path("blogs/update/<blog_id>", views.update_blog, name="update_blog"),
    path("blogs/delete/<blog_id>", views.delete_blog, name="delete_blog"),

]