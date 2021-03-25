from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from . models import Post, UserProfile

# Post Form---------------------


class PostForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class': 'form-control','placeholder':'Blog Title'})
    self.fields['cat'].widget.attrs.update({'class':'form-control'})    
    self.fields['thumb'].widget.attrs.update({'class':'form-input'})
    self.fields['banner'].widget.attrs.update({'class':'form-input'})
    self.fields['content'].widget.attrs.update({'class':'form-control','cols':'80','placeholder':'Blog Content','id':'bconid'})
    self.fields['tag'].widget.attrs.update({'class':'form-control','rows':'2','maxlength':'100','placeholder':'Blog tag:- Robotic, WifiStudy, Home made dish, diy projects'})
    self.fields['desc'].widget.attrs.update({'class':'form-control','rows':'2','maxlength':'100','placeholder':'Short description'})
    self.fields['pic1'].widget.attrs.update({'class':'media-input'})
    self.fields['pic2'].widget.attrs.update({'class':'media-input'})
    self.fields['pic3'].widget.attrs.update({'class':'media-input'})
    self.fields['pic4'].widget.attrs.update({'class':'media-input'})
    self.fields['pic5'].widget.attrs.update({'class':'media-input'})
     
  class Meta:
    model = Post
    fields = '__all__'
    # fields = ("title","cat","thumb","banner","content","tag")
    exclude = ['slug','feature','view','user','date','ready']
    labels = {
            'title': _('*Blog Title (max:100 words)'),
            'cat': _('*Categories'),
            'thumb': _('Thumbnails - 580X300'),
            'banner': _('Banner - 1920X500'),
            'content': _('*Blog Main Content'),
            'tag': _('Blog Tags'),
            'media': _('*Add Media'),
            'desc': _(' *Short Descriptions'),
            'pic1': _('Media Pic 1: '),
            'pic2': _('Media Pic 2: '),
            'pic3': _('Media Pic 3: '),
            'pic4': _('Media Pic 4: '),
            'pic5': _('Media Pic 5: '),
        }
   
    error_messages = {
        'title': {
            'max_length': _("This title's name is too long."),
        },
        'tag': {
            'max_length': _("Blog Tag's  is too long."),
        },
    }


class PostUpdateForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class': 'form-control','placeholder':'Blog Title'})
    self.fields['cat'].widget.attrs.update({'class':'form-control'})    
    self.fields['thumb'].widget.attrs.update({'class':'form-control'})
    self.fields['banner'].widget.attrs.update({'class':'form-control'})
    self.fields['content'].widget.attrs.update({'class':'form-control','cols':'80','placeholder':'Blog Content','id':'bconid'})
    self.fields['tag'].widget.attrs.update({'class':'form-control','rows':'2','maxlength':'100','placeholder':'Blog tag:- Robotic, WifiStudy, Home made dish, diy projects'})
    self.fields['desc'].widget.attrs.update({'class':'form-control','rows':'2','maxlength':'100','placeholder':'Short description'})
    self.fields['pic1'].widget.attrs.update({'class':'media-input'})
    self.fields['pic2'].widget.attrs.update({'class':'media-input'})
    self.fields['pic3'].widget.attrs.update({'class':'media-input'})
    self.fields['pic4'].widget.attrs.update({'class':'media-input'})
    self.fields['pic5'].widget.attrs.update({'class':'media-input'})
     
  class Meta:
    model = Post
    fields = '__all__'
    # fields = ("title","cat","thumb","banner","content","tag")
    exclude = ['slug','feature','view','user','date','ready']
    labels = {
            'title': _('*Blog Title (max:100 words)'),
            'cat': _('*Categories'),
            'thumb': _('Thumbnails - 580X300'),
            'banner': _('Banner - 1920X500'),
            'content': _('*Blog Main Content'),
            'tag': _('Blog Tags'),
            'media': _('*Add Media'),
            'desc': _(' *Short Descriptions'),
            'pic1': _('Media Pic 1: '),
            'pic2': _('Media Pic 2: '),
            'pic3': _('Media Pic 3: '),
            'pic4': _('Media Pic 4: '),
            'pic5': _('Media Pic 5: '),
        }
   
    error_messages = {
        'title': {
            'max_length': _("This title's name is too long."),
        },
        'tag': {
            'max_length': _("Blog Tag's  is too long."),
        },
    }


    
    class Meta:
        model = Post
        fields = ("__all__")


# Post Form---------------------





# User Form---------------------

# User logIn Form
class LoginForm(forms.Form):
  username = forms.CharField(
    min_length=4,
    max_length=50,
    required=True,
    label="Username",
    widget = forms.TextInput(
      attrs={'class':'form-control nmb-10','placeholder':'Username / email'}
    )
  ) 
  password = forms.CharField(
    min_length=4,
    max_length=50,
    required=True,
    label="Password",
    widget = forms.PasswordInput(
      attrs={'class':'form-control nmb-10','placeholder':'User Password'}
    )
  ) 


# User Registration Form 
class UserRegForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs.update({'class': 'form-control','placeholder':'First Name'})
    self.fields['last_name'].widget.attrs.update({'class': 'form-control','placeholder':'Last Name'})
    self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder':'Username'})
    self.fields['email'].widget.attrs.update({'class': 'form-control','placeholder':'Email'})
    self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder':'Set Password'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder':'Confirm Password'})

  class Meta:
    model = User
    fields = ['first_name','last_name','username','email','password1','password2']
    labels = {
      'first_name':'First Name',
      'last_name':'Last Name',
      'username':'User Name',
      'email':'Your Email',
      'password1':'Type Password',
      'password2':'Confirm Password',
      } 


class UserProfileForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['profilepic'].widget.attrs.update({'class': 'form-control'})
    self.fields['banner'].widget.attrs.update({'class': 'form-control'})
    self.fields['bio'].widget.attrs.update({'class': 'form-control'})
    self.fields['phone'].widget.attrs.update({'class': 'form-control'})
    self.fields['link1'].widget.attrs.update({'class': 'form-control'})
    self.fields['link2'].widget.attrs.update({'class': 'form-control'})
    self.fields['link3'].widget.attrs.update({'class': 'form-control'})
    self.fields['link4'].widget.attrs.update({'class': 'form-control'})

    self.fields['link1Icon'].widget.attrs.update({'class': 'form-control'})
    self.fields['link2Icon'].widget.attrs.update({'class': 'form-control'})
    self.fields['link3Icon'].widget.attrs.update({'class': 'form-control'})
    self.fields['link4Icon'].widget.attrs.update({'class': 'form-control'})


  iconChoice = (("fab fa-whatsapp","Icon: WhatsApp "),("fab fa-youtube","Icon: Youtube "),("fab fa-linkedin","Icon: LinkedIn "),("fab fa-github","Icon: Github "),("fab fa-instagram","Icon: Instagram"),("fab fa-twitter","Icon: Twitter"),("fas fa-envelope","Icon: Email"))
  
  
  link1Icon = forms.ChoiceField(label="Link 1 Icon : " ,choices=iconChoice, required=False)
  link2Icon = forms.ChoiceField(label="Link 2 Icon : " ,choices=iconChoice, required=False)
  link3Icon = forms.ChoiceField(label="Link 3 Icon : " ,choices=iconChoice, required=False)
  link4Icon = forms.ChoiceField(label="Link 4 Icon : " ,choices=iconChoice, required=False)
  userName = forms.CharField(widget=(forms.HiddenInput()))
 

  class Meta:
    model = UserProfile
    fields = '__all__'
    exclude=['verifyed']
    labels = {
      'profilepic':'Profile Image :',
      'banner':'Banner Image :',
      'bio':'Bio :',
      'phone':'Phone No :',
      'link1':'Social Link 1 :',
      'link2':'Social Link 2 :',
      'link3':'Social Link 3 :',
      'link4':'Social Link 4 :',        
      } 


class UserUpdateForm(UserChangeForm):







  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs.update({'class': 'form-control','placeholder':'First Name'})
    self.fields['last_name'].widget.attrs.update({'class': 'form-control','placeholder':'Last Name'})
    self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder':'Username'})
    self.fields['email'].widget.attrs.update({'class': 'form-control','placeholder':'Email'})

  class Meta:
    model = User
    fields = ['first_name','last_name','username','email']
# User  Form------------------------