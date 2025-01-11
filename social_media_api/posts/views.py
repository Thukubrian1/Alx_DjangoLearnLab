from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import filters
from .models import Post, Like
from rest_framework import generics
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.request.data['post'])
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        if self.get_object().author != self.request.user:
            raise PermissionDenied("You cannot edit this comment.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("You cannot delete this comment.")
        instance.delete()

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Get the post object by primary key (pk)
        post = get_object_or_404(Post, pk=pk)

        # Create or get the Like object, ensuring a user cannot like a post multiple times
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        # If the like is created, generate a notification
        if created:
            # Create a notification for the post author
            Notification.objects.create(
                recipient=post.author,  # The author of the post
                actor=request.user,  # The user who liked the post
                verb='liked',  # Describes the action
                target=post  # The post that was liked
            )
            return Response({"message": "Post liked successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'content']
    ordering_fields = ['created_at']

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Get the post object by primary key (pk)
        post = get_object_or_404(Post, pk=pk)

        # Try to retrieve the Like object, and delete it if it exists
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            
            # Optionally, you can create a notification for unliking the post or leave it out
            return Response({"message": "Like removed successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"message": "You haven't liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)
    
class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Get the users that the current user is following
        following_users = user.following.all()

        # Get posts from the followed users, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # Serialize the posts (assuming you already have a PostSerializer defined)
        from .serializers import PostSerializer
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)