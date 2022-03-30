from django.urls import path, include

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from rest_framework_sso.views import (
#     obtain_session_token,
#     obtain_authorization_token
# )

from . import views

urlpatterns = [
    path("users/<int:pk>", views.users_list, name="api_users"),
    path("users", views.user_create, name="api_create_user"),
    path("users/<int:user_id>/", views.user_update, name="api_update_user"),

    path("lists/<int:pk>", views.lists_list, name="api_lists"),
    path("lists", views.list_create, name="api_create_list"),
    path("lists/<int:pk>/", views.list_delete, name="api_delete_list"),

    path("lists/<int:pk>/items", views.item_list, name="api_item"),
    # path("session/", obtain_session_token),
    # path("authorize/", obtain_authorization_token),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]


# /api/v{n}/authenticate

# OK /api/v{n}/users/{ID} - GET
# OK /api/v{n}/users - POST - "first_name": STRING, "email": STRING, "username": STRING; "password": STRING
# OK /api/v{n}/users/{ID} - PUT - "name": STRING, "email": STRING, "login": STRING; "password": STRING

# OK /api/v{n}/lists/{ID} - GET
# /api/v{n}/lists - POST - "list" : { "title" : STRING }
# OK /api/v{n}/lists/{ID} - DELETE - "id": INTEGER

# /api/v{n}/lists/{ID}/items - GET
# /api/v{n}/lists/{ID}/items - POST - "title": STRING, "description": STRING, “user_id”: INTEGER
# /api/v{n}/lists/{ID}/items/{ID} - PUT - "title": STRING, "description": STRING, “user_id”: INTEGER
# /api/v{n}/lists/{ID}/items/{ID} - DELETE - "id": INTEGER
