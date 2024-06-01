from django.urls import path
from .views import signup, login, send_friend_request, accept_friend_request, reject_friend_request, list_friends, list_pending_requests, search_users

urlpatterns = [
    path('signup/', signup),
    path('login/', login),
    path('send_friend_request/<int:user_id>/', send_friend_request),
    path('accept_friend_request/<int:request_id>/', accept_friend_request),
    path('reject_friend_request/<int:request_id>/', reject_friend_request),
    path('list_friends/', list_friends),
    path('list_pending_requests/', list_pending_requests),
    path('search_users/', search_users),
]
