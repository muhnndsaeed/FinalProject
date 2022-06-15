from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Blog , Comment , Consultation , Profile ,ConComment
from .serializers import BlogSerializer , ConsultationSerializer , CommentSerializer ,ProfileSerializer,ConCommentSerializer
# Create your views here.

'''
 we use permission To verify the identity of the user
 
'''
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_profile(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('fitnessapp.add_profile'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)


    request.data["user"] = request.user.id

    new_profile = ProfileSerializer(data=request.data)
    if new_profile.is_valid():
        new_profile.save()
        dataResponse = {
            "msg": "Thank you for record Your Profile...",
            "Certification ": new_profile.data
        }
        return Response(dataResponse)
    else:
        print(new_profile.errors)
        dataResponse = {"msg": "Sorry, couldn't add new Profile"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_profile(request : Request):
    profile = Profile.objects.all()

    dataResponse = {
        "msg" : "List of All profiles",
        "profile": ProfileSerializer(instance=profile, many=True).data
    }

    return Response(dataResponse)




'''
To update the profile and confirm of id
'''
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_profile(request : Request, profile_id):
    profile = Profile.objects.get(id=profile_id)

    updated_profile = ProfileSerializer(instance=profile, data=request.data)
    if updated_profile.is_valid():
        updated_profile.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_profile.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


'''
to delete the profile by id 
'''

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_profile(request: Request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})




'''
Here you check if the user can create blog
If he has the permissions, the blog will be created
'''

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_blog(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('fitnessapp.add_blog'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)


    request.data["user"] = request.user.id

    new_blog = BlogSerializer(data=request.data)
    if new_blog.is_valid():
        new_blog.save()
        return Response({"Blog": new_blog.data})
    else:
        print(new_blog.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)


'''
to list all blogs
'''

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_blogs(request : Request):
    blogs = Blog.objects.all()

    dataResponse = {
        "msg" : "List of All blogs",
        "blogs" : BlogSerializer(instance=blogs, many=True).data
    }

    return Response(dataResponse)


'''
to update blog by id 
'''
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


'''
to delete the blog 
'''

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_blog(request: Request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return Response({"msg" : "Deleted Successfully"})




'''
to add consultaion 
If he has the permissions, the consultation will be created
'''
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_consultation(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('fitnessapp.add_consultation'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)


    request.data["user"] = request.user.id

    new_consultation = ConsultationSerializer(data=request.data)
    if new_consultation.is_valid():
        new_consultation.save()
        return Response({"Consultation": new_consultation.data})
    else:
        print(new_consultation.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)



'''
All consultations will be shown
'''
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_consultations(request : Request):
    consultation = Consultation.objects.all()

    dataResponse = {
        "msg" : "List of All consultations",
        "consultation": ConsultationSerializer(instance=consultation, many=True).data
    }

    return Response(dataResponse)


'''
to update consultation
'''
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_consultation(request : Request, consultation_id):
    consultation = Consultation.objects.get(id=consultation_id)

    updated_consultation = ConsultationSerializer(instance=consultation, data=request.data)
    if updated_consultation.is_valid():
        updated_consultation.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_consultation.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)



'''
To delete consulttion 
'''
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_consultation(request: Request, consultation_id):
    consultation = Consultation.objects.get(id=consultation_id)
    consultation.delete()
    return Response({"msg" : "Deleted Successfully"})





@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('fitnessapp.add_comment'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)


    request.data["user"] = request.user.id

    new_comment = CommentSerializer(data=request.data)
    if new_comment.is_valid():
        new_comment.save()
        return Response({"Comment": new_comment.data})
    else:
        print(new_comment.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_comment(request : Request):
    comments = Comment.objects.all()

    dataResponse = {
        "msg" : "List of All comments",
        "comments" : CommentSerializer(instance=comments, many=True).data
    }

    return Response(dataResponse)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_comment(request : Request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    updated_comment = CommentSerializer(instance=comment, data=request.data)
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


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_concomment(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('fitnessapp.add_concomment'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)


    request.data["user"] = request.user.id

    new_comment = ConCommentSerializer(data=request.data)
    if new_comment.is_valid():
        new_comment.save()
        return Response({"Comment": new_comment.data})
    else:
        print(new_comment.errors)

    return Response("no", status=status.HTTP_400_BAD_REQUEST)






@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_concomment(request : Request):
    comments = ConComment.objects.all()

    dataResponse = {
        "msg" : "List of All comments",
        "comments" : ConCommentSerializer(instance=comments, many=True).data
    }

    return Response(dataResponse)


'''

'''
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_concomment(request : Request, comment_id):
    comment = ConComment.objects.get(id=comment_id)

    updated_comment = ConCommentSerializer(instance=comment, data=request.data)
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
def delete_concomment(request: Request, comment_id):
    comment = ConComment.objects.get(id=comment_id)
    comment.delete()
    return Response({"msg" : "Deleted Successfully"})

