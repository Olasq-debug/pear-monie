from rest_framework.views import APIView
from rest_framework.permissions import BasePermission,IsAuthenticated
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from json import JSONDecodeError
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from appModel.models import User
import jwt, datetime, os
from dotenv import load_dotenv
load_dotenv()


# Create your views here.

class RegisterUsers(APIView):
    permission_classes = [BasePermission]
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = UserSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "json decode error"}, status=400)

# class LoginUsers(APIView):
#     def post(self, request):
#         try:
#             username = request['username']
#             password = request['password']
#             user = User.objects.filter(username=username).first()
#             if user is None:
#                 return Response({"message": "user does not exizts"}, status=status.HTTP_404_NOT_FOUND)
#             if not user.check_password(password):
               
#                 return Response({"message": 'Incorrect password'})
#             # payload = {
#             #     'id' : user.id,
#             #     "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             #     'iat': datetime.datetime.utcnow()
#             # }

#             # token = jwt.encode(payload=payload, key=os.environ.get("TOKEN_SECRET_KEY"),  algorithms=os.environ.get('ALGORITHMS'))
            
#             return Response({"message": "You are successfully logged in",}, data=user, status=status.HTTP_200_OK)
#         except Exception:
#             return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR )

        
    

