from django.urls import path
from . import views
from .views import ModifyUser


urlpatterns = [
    path("",views.get_all_users,name="get-all-users"),
    path("create_user",views.create_user,name="create-new-user"),
    path("user/<str:pk>",ModifyUser.as_view(),name="modify-user")
]
