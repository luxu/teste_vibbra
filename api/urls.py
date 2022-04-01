from django.urls import path, include

from . import views

urlpatterns = [
    path("times/", views.times, name="times"),
    # path("users", views.user_create, name="api_create_user"),
    # path("users/<int:user_id>/", views.user_update, name="api_update_user"),
    #
    # path("lists/<int:pk>", views.lists_list, name="api_lists"),
    # path("lists", views.list_create, name="api_create_list"),
    # path("lists/<int:pk>/", views.list_delete, name="api_delete_list"),
    #
    # path("lists/<int:pk>/items", views.item_list, name="api_item"),
    # path("session/", obtain_session_token),
    # path("authorize/", obtain_authorization_token),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

# /api/v{n}/authenticate
