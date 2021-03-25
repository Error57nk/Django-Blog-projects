from django.urls import path
from . import views as blogView

urlpatterns = [
    path("", blogView.index, name="home"),
    path("post/<str:slug>", blogView.viewPost, name="post"),
    path("post/<int:pk>/update/", blogView.PostUpdate.as_view(), name="post-update"),
    path("post/<str:slug>/delete/", blogView.PostDelete.as_view(), name="post-delete"),
    path("Post/new/", blogView.uploadPost, name="upload"),
    path("result/", blogView.viewResult, name="result"),
    path("profile/", blogView.userprofile, name="profile"),
    path("author/<str:buser>", blogView.authProfile, name="author"),
    path("profile/update/", blogView.updateUser, name="update-profile"),

    # User Urls
    path("logout/", blogView.logOutUser, name="logout"),
    path("login/", blogView.loginUser, name="login"),
    path("register/", blogView.userReg, name="register"),
    # path("post/update/<str:slug>", blogView.updatePost, name="post-update"),

    path("pt/", blogView.PostV.as_view()),
    # API___________________views

    path("api/post", blogView.postApiList, name='api-post-list'),
    
]
