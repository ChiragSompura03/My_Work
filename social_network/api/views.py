from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSignupSerializer, UserSerializer, FriendRequestSerializer
from .models import FriendRequest

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_friend_request(request, user_id):
    if FriendRequest.objects.filter(from_user=request.user, to_user_id=user_id, status='pending').exists():
        return Response({'error': 'Friend request already sent'}, status=status.HTTP_400_BAD_REQUEST)
    friend_request = FriendRequest(from_user=request.user, to_user_id=user_id)
    friend_request.save()
    return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user)
    if friend_request.status == 'pending':
        friend_request.status = 'accepted'
        friend_request.save()
        return Response(FriendRequestSerializer(friend_request).data)
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def reject_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user)
    if friend_request.status == 'pending':
        friend_request.status = 'rejected'
        friend_request.save()
        return Response(FriendRequestSerializer(friend_request).data)
    return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_friends(request):
    friends = FriendRequest.objects.filter(
        (models.Q(from_user=request.user) | models.Q(to_user=request.user)) & models.Q(status='accepted')
    )
    users = [req.to_user if req.from_user == request.user else req.from_user for req in friends]
    return Response(UserSerializer(users, many=True).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_pending_requests(request):
    pending_requests = FriendRequest.objects.filter(to_user=request.user, status='pending')
    return Response(FriendRequestSerializer(pending_requests, many=True).data)


class UserPagination(PageNumberPagination):
    page_size = 10


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_users(request):
    keyword = request.query_params.get('keyword', '')
    if '@' in keyword:
        users = User.objects.filter(email__iexact=keyword)
    else:
        users = User.objects.filter(models.Q(first_name__icontains=keyword) | models.Q(last_name__icontains=keyword))
    paginator = UserPagination()
    result_page = paginator.paginate_queryset(users, request)
    return paginator.get_paginated_response(UserSerializer(result_page, many=True).data)

