from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.forms.models import model_to_dict
from datetime import date, datetime, timedelta
import uuid

from .models import User
from .serializers import *

@api_view(['GET', 'POST'])
def user_signup(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if "ExpirationAccess" not in request.data:
            request.data["ExpirationAccess"] = date.today() + timedelta(weeks=2)

        request.data["TokenAccess"] = str(uuid.uuid4())
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    try:
        user = User.objects.get(UserAccess=request.data.get("UserAccess"),PassAccess=request.data.get("PassAccess"))
    except User.DoesNotExist:
        return Response({"estado":"false","descripcionRespuesta":"Usuario o contrasena incorrecto"},status=status.HTTP_404_NOT_FOUND)

    if datetime.now() > datetime.combine(user.ExpirationAccess, datetime.min.time()):
        user.ExpirationAccess = date.today() + timedelta(weeks=2)
        user.TokenAccess = str(uuid.uuid4())

        serializer = UserSerializer(user, data=model_to_dict(user))
        serializer.is_valid()
        serializer.save()

    return Response({"estado":"true","descripcionRespuesta":"","token":serializer.data.get("TokenAccess")})