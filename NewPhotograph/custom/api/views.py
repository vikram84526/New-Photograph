from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from custom.models import UserDetails
from .serializers import  UserDetailsSerializer



class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}

        username = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(username=username, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Exception as e:
                token = Token.objects.create(user=account)
            context['token'] = token.key
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'


        return Response(context)

@api_view(['PUT',])
def  updateuserdetails(request,slug):
    try:
        user_post = UserDetails.objects.get(user_id__username=slug)
    except UserDetails.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)


    if request.method=="PUT":
        serializer = UserDetailsSerializer(user_post,data = request.data)
        data ={}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "update successful"
            return Response(data=data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
def  deleteuserdetails(request,slug):
    try:
        user_post = UserDetails.objects.get(user_id__username=slug)
    except UserDetails.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method=="DELETE":
        opt = user_post.delete()
        data ={}
        if opt:
            data['success'] = "delete successful"
        else:
            data['failure'] = "delete failed"
        return Response(data=data)







