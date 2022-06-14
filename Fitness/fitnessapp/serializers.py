from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Blog , Comment , Consultation , ConComment


class UserSerializerView(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consultation
        fields = '__all__'

class ConCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConComment
        fields = '__all__'

