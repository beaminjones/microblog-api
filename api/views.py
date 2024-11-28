from .serializers import PostSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .models import Post, User

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "Login realizado com sucesso!"}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        return Response({"message": "Usuário cadastrado!"})

class FollowUserView(APIView):
    def post(self, request):
        return Response({"message": "Seguindo usuário!"})

class CreatePostView(APIView):
    def post(self, request):
        return Response({"message": "Post criado!"})

class LikePostView(APIView):
    def post(self, request):
        return Response({"message": "Post Curtido!"})

class CommentPostView(APIView):
    def post(self, request):
        return Response({"message": "Post comentado!"})

class FeedView(APIView):
    def get(self, request, user_id):
        user = User.objects.filter(id=user_id).first()
        
        if not user:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        user_posts = Post.objects.filter(author=user)

        if user.following.exists():
            friends_posts = Post.objects.filter(author__in=user.following.all())
        else:
            friends_posts = Post.objects.none()

        all_posts = user_posts | friends_posts
        all_posts = all_posts.order_by('-created_at')

        serializer = PostSerializer(all_posts, many=True)

        if not user_posts:
            return Response({"error": "Nenhum post encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)