from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image
from django.urls import reverse
# Create your models here.
class UserProfile(models.Model):
  userName = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
  # name = models.CharField(max_length=50,default="User",null=True)
  profilepic = models.ImageField(upload_to="blog/userPic", default="profile.png",null=True,blank = True)
  banner = models.ImageField(upload_to="blog/userBanner", default="banner.jpg",null=True,blank = True)
  bio = models.TextField(max_length=500,null = True)
  phone = models.CharField(max_length=12,default = "" ,null = True)
  verifyed = models.BooleanField(default= False)
  link1 = models.CharField(max_length=100, default="https://wa.me/", null=True)
  link1Icon = models.CharField(
      max_length=100, default="fab fa-whatsapp", blank=True
  )

  link2 = models.CharField(
      max_length=100, default="https://www.youtube.com/", null=True
  )
  link2Icon = models.CharField(max_length=100, default="fab fa-youtube", blank=True)

  link3 = models.CharField(
      max_length=100, default="https://www.linkedin.com/in/", null=True
  )
  link3Icon = models.CharField(
      max_length=100, default="fab fa-linkedin", blank=True
  )

  link4 = models.CharField(
      max_length=100, default="https://www.github.com/", null=True
  )
  link4Icon = models.CharField(max_length=100, default="fab fa-github", blank=True)

  def __str__(self):
    return self.userName.username

class BlogCategory(models.Model):
  cat = models.CharField(unique=True,max_length=100)
  catImg = models.ImageField(upload_to="blog/categoryImage", default="picture_1457X446.jpg")
  des = models.TextField(max_length=200, blank=True, null=True)
  def __str__(self):
    return self.cat
  def save(self,*args,**kwargs):
    super().save(*args,**kwargs)
    pic_cat = Image.open(self.catImg.path)
    
    if pic_cat.height > 40 or pic_cat.width > 276:
      output_size = (40, 276)
      pic_cat.thumbnail(output_size)
      pic_cat.save(self.catImg.path)


class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=250)
  desc = models.TextField(max_length=250, default="")
  slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
  cat = models.ForeignKey(BlogCategory, on_delete= models.SET_NULL,null=True)
  date = models.DateField(auto_now_add=True, null=True)
  content = models.TextField(max_length=3000)
  thumb = models.ImageField(upload_to="blog/postthumb", default="thumb.png")
  banner = models.ImageField(upload_to="blog/postbanner", default="banner.png")
  view = models.IntegerField(default=0)
  tag = models.TextField(max_length=200,null=True,blank = True)
  pic1 = models.ImageField(upload_to="blog/postpic", default="",null=True,blank = True)
  pic2 = models.ImageField(upload_to="blog/postpic", default="",null=True,blank = True)
  pic3 = models.ImageField(upload_to="blog/postpic", default="",null=True,blank = True)
  pic4 = models.ImageField(upload_to="blog/postpic", default="",null=True,blank = True)
  pic5 = models.ImageField(upload_to="blog/postpic", default="",null=True,blank = True)
  feature = models.BooleanField(default=False)
  ready = models.BooleanField(default=False)
  media = models.BooleanField(default=False)

  def __str__(self):
      return self.title
  
  def get_absolute_url(self):
    return reverse('post', kwargs={'slug':self.slug})

  @property
  def tagList(self):
      return self.tag.split(",")
  @property
  def userName(self):
      return self.user.username
  @property
  def catName(self):
      return self.cat.cat
  

  def save(self,*args,**kwargs):
    val = self.title
    try:
      self.slug=slugify(val, allow_unicode=True)
    except:
      self.slug=slugify(val + "efx", allow_unicode=True)
    
    super().save(*args,**kwargs)

   


# h=380 b=850



  
  
