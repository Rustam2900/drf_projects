from rest_framework import generics, views, status, permissions
from rest_framework.response import Response
from users import models, serializers


class RegisterApiView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save(), status=status.HTTP_201_CREATED)


class ProfileApiView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = models.User.objects.get(id=request.user.id)
        serializer = serializers.ProfileSerializer(user)
        return Response(serializer.data)

