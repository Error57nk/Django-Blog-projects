from django.contrib import admin
from .models import *


admin.site.site_header = "PortFolio Admin"


class AdminBio(admin.ModelAdmin):
    fields = (
        "name",
        "tagLine",
        "areaIntrest",
        "profilePic",
        "admin_photo",
        "bannerPic",
        "biobanner",
        "bioindex",
        "bioabout",
        "email1",
        "email2",
        "phone1",
        "phone2",
        "address",
    )
    list_display = ["id", "admin_photo", "name", "phone1", "email1"]
    list_display_links = ["name", "email1"]
    list_filter = ["name", "email1"]
    data_hierarchy = "email1"
    readonly_fields = ("admin_photo",)


class AdminEducation(admin.ModelAdmin):
    list_display = ["degree", "instituteName", "year"]


class AdminSkillSet(admin.ModelAdmin):
    list_display = ["tittle"]


class AdminProCat(admin.ModelAdmin):
    list_display = ["id", "cat"]


class AdminLanguage(admin.ModelAdmin):
    list_display = ["id", "title", "des"]


class AdminHobbies(admin.ModelAdmin):
    list_display = ["user", "title", "tag"]


class AdminProjects(admin.ModelAdmin):
    list_display = ["cat", "title", "feture", "proLink"]


class AdminCertificates(admin.ModelAdmin):
    list_display = ["title", "date"]


class AdminSocialLink(admin.ModelAdmin):
    list_display = ["user", "whatsapp", "linkedin", "youtube", "github"]


# Register your models here.

admin.site.register(Bio, AdminBio)

admin.site.register(Education, AdminEducation)
admin.site.register(SkillSet, AdminSkillSet)
admin.site.register(ProCat, AdminProCat)
admin.site.register(Projects, AdminProjects)
admin.site.register(Certificates, AdminCertificates)
admin.site.register(SocialLink, AdminSocialLink)
admin.site.register(Hobbies, AdminHobbies)
admin.site.register(Language, AdminLanguage)
