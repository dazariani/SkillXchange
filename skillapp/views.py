from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .serializers import SkillClassSerializer, ReviewSerializer, EnrollmentSerializer, UserSerializer
from .models import SkillClass, Review, Enrollment, CustomUser
from .permissions import SkillClassPermissionObjLevel, SkillClassPermissionModelLevel, EnrollmentPermissionObjLevel, EnrollmentPermissionModelLevel, ReviewPermissionObjLevel, ReviewPermissionModelLevel
from rest_framework.exceptions import AuthenticationFailed

# Model ViewSets
class SkillClassViewSet(viewsets.ModelViewSet):
    queryset = SkillClass.objects.all()
    serializer_class = SkillClassSerializer
    permission_classes = [SkillClassPermissionObjLevel & SkillClassPermissionModelLevel]


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [EnrollmentPermissionObjLevel, EnrollmentPermissionModelLevel]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewPermissionObjLevel, ReviewPermissionModelLevel]


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# Login
class CustomAuthToken(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token,create = Token.objects.get_or_create(user=user)
            return Response({'Token': token.key})
        else:
            return Response({'error': 'Invalid Credentials :('}, status=status.HTTP_400_BAD_REQUEST)
        

# Register
class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user:
                token,create = Token.objects.get_or_create(user=user)
                return Response({'Token': token.key})
        else:
            return Response({'error': 'Invalid Credentials :('}, status=status.HTTP_400_BAD_REQUEST)
        

# Current user
class UserView(APIView):
    def get(self, request): 
        if not request.user.id:
            raise AuthenticationFailed('Unauthenticated :(')
        
        user = CustomUser.objects.filter(id=request.user.id).first()

        serializer = UserSerializer(user)

        return Response(serializer.data)
