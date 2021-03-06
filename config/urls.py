"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import views as post_view
from group import views
from saidituser import views as user_view
from authorization_app import views as auth_view
from reply import views as reply_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('userdetail/<int:id>/edit/', user_view.edit_userview),
    path('userdetail/<int:id>/', user_view.userview, name='user-detail'),
    path('join/<int:id>/', views.join_group, name="join-group"),
    path("leavegroup/<int:id>/", views.leave_group, name="leave-group"),
    path('addpost/<int:id>/', post_view.addPost, name="new-post"),
    path('', post_view.index, name='home'),
    path('admin/', admin.site.urls),
    path('addgroup/', views.addSubgroup),
    path('groupdetail/<int:id>/', views.group_detail, name='group-detail'),
    path('login/', auth_view.login_view, name='login'),
    path('logout/', auth_view.logout_view, name='logout'),
    path('signup/', auth_view.signup_view, name='signup'),
    path('accounts/', include('allauth.urls')),
    path("post/<int:post_id>/", post_view.PostView.as_view(), name="post"),
    path("replydetail/<int:reply_id>/", reply_view.ReplyDetailView.as_view(), name="reply-detail"),
    path("createreply/<int:reply_id>/", reply_view.create_reply, name="new-reply"),
    path("initiatereply/<int:post_id>/", reply_view.initiate_reply, name="initiate-reply"),
    path("followers/<int:id>/", user_view.FollowerList.as_view()),
    path("<int:id>/like/", post_view.like_count),
    path("<int:id>/dislike/", post_view.dislike_count),
    path("<int:id>/like-reply/", reply_view.toggle_like),
    path("following/<int:id>/", user_view.FollowingList.as_view()),
    path('follow/<int:id>/', user_view.follow, name="follow"),
    path('unfollow/<int:id>/', user_view.unfollow, name="follow"),
    path("groups/", views.GroupListView.as_view(), name="groups"), 
    path("userprofile/<int:id>/", user_view.userview, name="profile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()


handler404 = "saidituser.views.handle_not_found"
handler500 = "saidituser.views.error_500"