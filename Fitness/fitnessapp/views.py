from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Blog , Comment
from .serializers import BlogSerializer
# Create your views here.

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_blog(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    print(request.user.is_staff)


    new_blog = BlogSerializer(data=request.data)
    if new_blog.is_valid():
        new_blog.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "blog" : new_blog.data
        }
        return Response(dataResponse)
    else:
        print(new_blog.errors)
        dataResponse = {"msg" : "couldn't create a blog"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_blogs(request : Request):
    blogs = Blog.objects.all()

    dataResponse = {
        "msg" : "List of All blogs",
        "blogs" : BlogSerializer(instance=blogs, many=True).data
    }

    return Response(dataResponse)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_blog(request : Request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    updated_blog = BlogSerializer(instance=blog, data=request.data)
    if updated_blog.is_valid():
        updated_blog.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_blog.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_blog(request: Request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return Response({"msg" : "Deleted Successfully"})




@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_comment(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    print(request.user.is_staff)


    new_comment = CommentSerializer(data=request.data)
    if new_comment.is_valid():
        new_comment.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "comment" : new_comment.data
        }
        return Response(dataResponse)
    else:
        print(new_comment.errors)
        dataResponse = {"msg" : "couldn't create a comment"}
        return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_comment(request : Request):
    blogs = Comment.objects.all()

    dataResponse = {
        "msg" : "List of All comments",
        "comments" : BlogSerializer(instance=blogs, many=True).data
    }

    return Response(dataResponse)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_comment(request : Request, comment_id):
    blog = Comment.objects.get(id=comment_id)

    updated_comment = BlogSerializer(instance=blog, data=request.data)
    if updated_comment.is_valid():
        updated_comment.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_comment.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_comment(request: Request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return Response({"msg" : "Deleted Successfully"})



