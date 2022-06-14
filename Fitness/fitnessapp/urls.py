from django.urls import path
from . import views

app_name = "fitnessapp"

urlpatterns = [
    path("profile/add",views.add_profile,name="Add profile"),
    path("profile/all",views.list_profile,name="list profiles"),
    path("profile/update/<profile_id>", views.update_profile,name="update_profile"),
    path("profile/delete/<profile_id>", views.delete_profile,name="delete_profile"),
    path("blogs/add", views.add_blog, name="Add blog"),
    path("blogs/all", views.list_blogs, name="list blogs"),
    path("blogs/update/<blog_id>", views.update_blog, name="update_blog"),
    path("blogs/delete/<blog_id>", views.delete_blog, name="delete_blog"),
    path("comment/add",views.add_comment, name="Add comment"),
    path("comment/all",views.list_comment,name= "list comments"),
    path("comment/update/<comment_id>",views.update_comment, name="update_comment"),
    path("comment/delete/<comment_id>", views.delete_comment,name= "delete_comment"),
    path("consultation/add", views.add_consultation, name="Add consultation"),
    path("consultation/all",views.list_consultations,name="list consultations"),
    path("consultation/update/<consultation_id>",views.update_consultation,name="update_consultation"),
    path("consultation/delete/<consultation_id>",views.delete_consultation,name="delete_consultation"),
    path("concomment/add",views.add_concomment, name="Add comment"),
    path("concomment/all",views.list_concomment,name= "list comments"),
    path("concomment/update/<comment_id>",views.update_concomment, name="update_comment"),
    path("concomment/delete/<comment_id>", views.delete_concomment,name= "delete_comment"),


]