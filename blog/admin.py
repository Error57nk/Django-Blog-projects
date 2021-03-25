from django.contrib import admin
from .models import *


admin.site.site_header = "Blog Admin"

class AdminBlogUser(admin.ModelAdmin):
    list_display = ["id","userName","profilepic","banner"]
# class AdminSocialLink(admin.ModelAdmin):
#     list_display = ["user", "link1","link2","link3","link4"]
class AdminBlogCategory(admin.ModelAdmin):
    list_display = ["cat", "catImg","des"]
class AdminPost(admin.ModelAdmin):
    list_display = ["id","user", "title","ready","feature","view"]
# class AdminPostMedia(admin.ModelAdmin):
#     list_display = ["postid", "pic1","pic2","pic3","pic4","pic5"]


# Register your models here.

admin.site.register(UserProfile, AdminBlogUser)
# admin.site.register(SocialLink, AdminSocialLink)
admin.site.register(BlogCategory, AdminBlogCategory)
admin.site.register(Post, AdminPost)
# admin.site.register(PostMedia, AdminPostMedia)
