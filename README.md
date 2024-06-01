Title:- API for social networking application using Django Rest Framework

Introduction:-
This project is aimed at creating a robust API for a social networking application using Django Rest Framework (DRF). Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. DRF is a powerful toolkit for building Web APIs in Django, providing a set of tools and functionalities for easily creating APIs.


Description:- 
The project aims to develop an API backend for a social networking application. The API will provide endpoints for various features commonly found in social networking platforms, such as user authentication, creating and managing user profiles, posting, commenting, following other users, etc.

API Endpoints:-
/signup/ - User Signup 
/login/ - User Login
/send_friend_request/<user_id>/ - Send Friend Request
/accept_friend_request/<request_id>/ - Accept Friend Request
/reject_friend_request/<request_id>/ - Reject Friend Request
/list_friends/ - List Friends
/list_pending_requests/ - List Pending Friend Requests
/search_users/ - Search Users by Email or Name


Usage:-

Signup:-
Method: POST
URL: http://localhost:8000/signup/
Body (JSON):
{
    "email": "test@example.com",
    "password": "password123"
}


Login:
Method: POST
URL: http://localhost:8000/login/
Body (JSON):
{
    "email": "test@example.com",
    "password": "password123"
}
Response should contain a token:
{
    "token": "your_generated_token"
}


Send Friend Request:
Method: POST
URL: http://localhost:8000/send_friend_request/<user_id>/
Headers: Authorization: Token your_generated_token


Accept Friend Request:
Method: POST
URL: http://localhost:8000/accept_friend_request/<request_id>/
Headers: Authorization: Token your_generated_token


Reject Friend Request:
Method: POST
URL: http://localhost:8000/reject_friend_request/<request_id>/
Headers: Authorization: Token your_generated_token


List Friends:
Method: GET
URL: http://localhost:8000/list_friends/
Headers: Authorization: Token your_generated_token


List Pending Friend Requests:
Method: GET
URL: http://localhost:8000/list_pending_requests/
Headers: Authorization: Token your_generated_token


Search Users:
Method: GET
URL: http://localhost:8000/search_users/?keyword=test
Headers: Authorization: Token your_generated_token

