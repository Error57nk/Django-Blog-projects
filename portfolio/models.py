from django.db import models
from django.utils.safestring import mark_safe


class Bio(models.Model):
    name = models.CharField(max_length=100)
    tagLine = models.CharField(max_length=100, null=True)
    profilePic = models.ImageField(
        upload_to="portfolio/profilePic", default="picture_220X220.jpg"
    )
    bannerPic = models.ImageField(
        upload_to="portfolio/bannerPic", default="picture_1457X446.jpg"
    )
    biobanner = models.TextField(max_length=200, blank=True, null=True)
    bioindex = models.TextField(max_length=500, blank=True, null=True)
    bioabout = models.TextField(max_length=700, blank=True, null=True)
    email1 = models.EmailField(max_length=100, unique=True)
    email2 = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200)
    phone1 = models.CharField(max_length=12, default="", unique=True)
    phone2 = models.CharField(max_length=12, default="empty", blank=True, null=True)
    areaIntrest = models.TextField(
        max_length=300, default="Electronic", blank=True, null=True
    )

    def admin_photo(self):
        return mark_safe('<img src="{}" width=100 />'.format(self.profilePic.url))

    admin_photo.short_description = "Image"
    admin_photo.allow_tag = True

    @property
    def profileImgURL(self):
        try:
            url = self.profilePic.url
        except:
            url = ""
        return url

    @property
    def areaIntrestList(self):
        return self.areaIntrest.split(",")

    @property
    def bannerImgURL(self):
        try:
            url = self.bannerPic.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.name


class SkillSet(models.Model):
    user = models.ForeignKey(Bio, on_delete=models.SET_NULL, null=True)
    tittle = models.CharField(max_length=100, default="")
    logo_class = models.CharField(
        max_length=50, default="fas fa-shield-alt", blank=True, null=True
    )

    def __str__(self):
        return self.tittle


class ProCat(models.Model):
    cat = models.CharField(max_length=100)
    des = models.TextField(max_length=300, blank=True, null=True)
    feture_pic = models.ImageField(
        upload_to="portfolio/Feature",
        default="picture_64X64.jpg",
        blank=True,
        null=True,
    )

    def fetureImgURL(self):
        try:
            url = self.feture_pic.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.cat


class Projects(models.Model):
    user = models.ForeignKey(Bio, on_delete=models.SET_NULL, null=True)
    cat = models.ForeignKey(ProCat, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="")
    project_pic = models.ImageField(
        upload_to="portfolio/projects",
        default="picture_500X300.jpg",
        blank=True,
        null=True,
    )
    feture_pic = models.ImageField(
        upload_to="portfolio/Feature",
        default="picture_300X300.jpg",
        blank=True,
        null=True,
    )
    des = models.TextField(max_length=500)
    techused = models.TextField(max_length=100)
    proLink = models.CharField(
        max_length=100, default="javascript:void(0)", blank=True, null=True
    )
    proGithub = models.CharField(
        max_length=100, default="https://github.com/Error57nk", blank=True, null=True
    )
    proStatus = models.CharField(
        max_length=100, default="Completed", blank=True, null=True
    )
    proDownload = models.CharField(
        max_length=100, default="Only For Android", blank=True, null=True
    )
    feture = models.BooleanField(default=False, null=True)

    @property
    def fetureImgURL(self):
        try:
            url = self.feture_pic.url
        except:
            url = ""
        return url

    @property
    def techusedList(self):
        return self.techused.split(",")

    @property
    def projectImgURL(self):
        try:
            url = self.project_pic.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.title


class Certificates(models.Model):
    user = models.ForeignKey(Bio, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="")
    institute = models.CharField(max_length=100, blank=True, null=True)
    des = models.TextField(max_length=300, blank=True, null=True)
    Images = models.ImageField(
        upload_to="portfolio/certificates", default="picture_400X300.jpg"
    )
    date = models.DateField(blank=True, null=True)

    @property
    def certiImgURL(self):
        try:
            url = self.Images.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.title


class Education(models.Model):
    user = models.ForeignKey(Bio, on_delete=models.SET_NULL, null=True)
    degree = models.CharField(max_length=100)
    branch = models.CharField(max_length=100, blank=True, null=True)
    instituteName = models.CharField(max_length=100, null=True)
    board = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    subjectdes = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(default=0)
    iconsPic = models.ImageField(
        upload_to="portfolio/icons", default="picture_64X64.jpg", blank=True, null=True
    )

    @property
    def iconImgURL(self):
        try:
            url = self.iconsPic.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.degree


class SocialLink(models.Model):
    user = models.OneToOneField(Bio, on_delete=models.SET_NULL, null=True)

    whatsapp = models.CharField(max_length=100, default="https://wa.me/", null=True)
    whatsappIcon = models.CharField(
        max_length=100, default="fab fa-whatsapp", blank=True
    )

    youtube = models.CharField(
        max_length=100, default="https://www.youtube.com/", null=True
    )
    youtubeIcon = models.CharField(max_length=100, default="fab fa-youtube", blank=True)

    linkedin = models.CharField(
        max_length=100, default="https://www.linkedin.com/in/", null=True
    )
    linkedinIcon = models.CharField(
        max_length=100, default="fab fa-linkedin", blank=True
    )

    github = models.CharField(
        max_length=100, default="https://www.github.com/", null=True
    )
    githubIcon = models.CharField(max_length=100, default="fab fa-github", blank=True)

    def __str__(self):
        return self.user.name


class Hobbies(models.Model):
    user = models.ForeignKey(Bio, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="")
    images = models.ImageField(
        upload_to="portfolio/hobbies", default="picture_350X200.jpg"
    )
    des = models.TextField(max_length=200, blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)

    @property
    def hobbiesImgURL(self):
        try:
            url = self.images.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.title


class Language(models.Model):
    user = models.ForeignKey(Bio, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, default="English")
    des = models.CharField(max_length=100, default="Read, Write, Speak", null=True)

    def __str__(self):
        return self.title
