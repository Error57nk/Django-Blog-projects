from django.http import request, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# from django.http import JsonResponse
from .models import (
    Bio,
    SkillSet,
    Projects,
    SocialLink,
    Education,
    Certificates,
    Hobbies,
    Language,
)

# Create your views here.
# mailId = "subham@gmail.com"
mailId = "niteshkrsit@gmail.com"


def index(request):
    bio = Bio.objects.filter(email1=mailId).first()

    user = bio.id
    skill = SkillSet.objects.filter(user=user)
    pro = Projects.objects.filter(user=user, feture=True)[:6]
    slink = SocialLink.objects.filter(user=user).first()

    # imgGallery = Projects.objects.filter(user=user, feture=True)[5]
    context = {"bio": bio, "skill": skill, "pro": pro, "slink": slink}
    return render(request, "portfolio/index.html", context)


def about(request):
    bio = Bio.objects.filter(email1=mailId).first()
    user = bio.id
    skill = SkillSet.objects.filter(user=user)
    pro = Projects.objects.filter(user=user, feture=True)[:12]
    slink = SocialLink.objects.filter(user=user).first()
    edu = Education.objects.filter(user=user)
    certi = Certificates.objects.filter(user=user)[:4]
    hoby = Hobbies.objects.filter(user=user)

    # imgGallery = Projects.objects.filter(user=user, feture=True)[5]
    context = {
        "bio": bio,
        "skill": skill,
        "pro": pro,
        "slink": slink,
        "edu": edu,
        "certi": certi,
        "hobbies": hoby,
        "user": user,
    }
    return render(request, "portfolio/about.html", context)


def projects(request):
    bio = Bio.objects.filter(email1=mailId).first()
    user = bio.id
    slink = SocialLink.objects.filter(user=user).first()

    proweb = Projects.objects.filter(user=user, cat=1)[:2]
    pwCount = Projects.objects.filter(user=user, cat=1).count()

    proapp = Projects.objects.filter(user=user, cat=2)[:2]
    paCount = Projects.objects.filter(user=user, cat=2).count()

    prohard = Projects.objects.filter(user=user, cat=3)[:2]
    phCount = Projects.objects.filter(user=user, cat=3).count()

    proiot = Projects.objects.filter(user=user, cat=4)[:2]
    piCount = Projects.objects.filter(user=user, cat=4).count()

    proother = Projects.objects.filter(user=user, cat=5)[:2]
    poCount = Projects.objects.filter(user=user, cat=5).count()

    CountObj = {
        "pwCount": pwCount,
        "paCount": paCount,
        "phCount": phCount,
        "piCount": piCount,
        "poCount": poCount,
    }
    # imgGallery = Projects.objects.filter(user=user, feture=True)[5]
    context = {
        "bio": bio,
        "proweb": proweb,
        "proapp": proapp,
        "prohard": prohard,
        "proiot": proiot,
        "proother": proother,
        "slink": slink,
        "pCount": CountObj,
        "user": user,
    }
    return render(request, "portfolio/projects.html", context)


def resume(request):
    bio = Bio.objects.filter(email1=mailId).first()
    user = bio.id
    pro = Projects.objects.filter(user=user, feture=True).values_list("title", "des")[
        :4
    ]
    skill = SkillSet.objects.filter(user=user)
    slink = SocialLink.objects.filter(user=user).first()
    edu = Education.objects.filter(user=user)
    lang = Language.objects.filter(user=user)
    certi = Certificates.objects.filter(user=user).values_list("title", "institute")[:4]

    context = {
        "bio": bio,
        "slink": slink,
        "pro": pro,
        "skill": skill,
        "edu": edu,
        "certi": certi,
        "lang": lang,
    }
    return render(request, "portfolio/resume.html", context)


def contact(request):
    info = "Nitesh Kumar"
    context = {"info": info}
    return render(request, "portfolio/contact.html", context)


def noLink(request):
    return HttpResponse(
        "<h2 style='color: red;'><span style='color: #333;'>Error57nk :</span> Page Not Found</h2>"
    )


# EXtra Work Loding Fetching


def load_certi(request):
    offset = int(request.POST["offset"])
    user = int(request.POST["user"])
    limit = 4
    certi = Certificates.objects.filter(user=user)[offset : limit + offset]
    totalData = Certificates.objects.filter(user=user).count()
    data = {}
    post_json = serializers.serialize("json", certi)
    return JsonResponse(
        data={"getCerti": post_json, "totalCerti": totalData, "user": user}
    )


def load_pro(request):
    offset = int(request.POST["offset"])
    user = int(request.POST["user"])
    rcat = request.POST["cat"]
    cat = 0
    if rcat == "web":
        cat = 1
    elif rcat == "app":
        cat = 2
    elif rcat == "hard":
        cat = 3
    elif rcat == "iot":
        cat = 4
    else:
        cat = 5

    limit = 2
    proweb = Projects.objects.filter(user=user, cat=1)
    proData = Projects.objects.filter(user=user, cat=cat)[offset : limit + offset]

    data = {}
    post_json = serializers.serialize("json", proData)
    return JsonResponse(data={"getPro": post_json, "user": user})
