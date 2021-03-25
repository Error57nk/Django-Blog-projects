from django.http import request, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView, UpdateView, ListView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator

from . models import Post, UserProfile, BlogCategory
from . forms import PostForm,PostUpdateForm,LoginForm,UserRegForm,UserProfileForm,UserUpdateForm
from django.contrib import messages

# API Lib
from .serializers import PostSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    post = Post.objects.filter(ready=True).order_by('-date')
    pop_post = Post.objects.filter(ready=True).order_by('-view')[:4]
    res_post = Post.objects.filter(ready=True).order_by('-date')[:4]
    fp = Post.objects.filter(feature=True,ready=True)[:3]
    cat = BlogCategory.objects.all()
    paginator = Paginator(post, 6, orphans=2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {"post":page_obj,"cat":cat,"ppost":pop_post,"rpost":res_post,"fp":fp}
    return render(request, 'blog/index.html',context)



def viewPost(request, slug):
    post = Post.objects.filter(slug = slug).first()
    if post:
      
        if post.user:
            currentuser = User.objects.filter(username=post.user).first()
            userProfile = UserProfile.objects.filter(userName=currentuser).first()
            if post.ready:
                cview = post.view + 1
                Post.objects.filter(slug = slug).update(view=cview)
                print(cview)
            postuser =  Post.objects.filter(user = currentuser, ready=True)[:4]
            postcat = Post.objects.filter(cat = post.cat, ready=True)[:4]
            cat = BlogCategory.objects.all()
        else:
            return render(request,"blog/404page.html",{"error":"Post Error"})
        
        # soc =
        context={
            "post":post,
            "postuser":postuser,
            "postcat":postcat,
            "cat":cat,
            "userdata":userProfile
        }
        return render(request,"blog/view-post.html",context)
    else:
        return redirect(index)



class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # fields =['title','content','desc','thumb','banner','tag','cat']
    template_name ='blog/upload-post.html'
    form_class = PostUpdateForm
    success_url = '/profile/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    def form_valid(self, form):                
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['update'] = True
        return context   


class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name ='blog/post-delete.html'
    success_url = '/profile/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False



def authProfile(request, buser):
    currentuser = User.objects.filter(username=buser).first()
    print(currentuser)
    if currentuser and currentuser != None:           
        userId = currentuser.id       
        try:
            userprofile = UserProfile.objects.get(userName=userId)

            # Total Post
            tpost = Post.objects.filter(user=userId, ready=True).count()


            #User Post
            
            if(userId == request.user.id):
                post = Post.objects.filter(user=userId).order_by('-date')[:10]
            else:
                post = Post.objects.filter(user=userId, ready=True).order_by('-date')[:10]
            

            #popular post/Recent Post
            pop_post = Post.objects.filter(ready=True).order_by('-view')[:4]
          
            res_post = Post.objects.filter(ready=True).order_by('-date')[:4]
            cat = BlogCategory.objects.all()
    
            paginator = Paginator(post, 10, orphans=2)
            page_num = request.GET.get('page')
            page_obj = paginator.get_page(page_num)

            # .values_list('userName','name','profilepic','banner','bio',flat=True)[0]
            context={"userdata":currentuser,"userprofile":userprofile,"tpost":tpost,"post":page_obj,"cat":cat,"ppost":pop_post,"rpost":res_post,"profile":True}

            return render(request,"blog/profile.html",context)
          
        except:
            print("exception")
            #categories
            return render(request,"blog/404page.html",{"error":buser})
       
    else:
        return render(request,"blog/404page.html",{"error":buser})

 
    
def viewResult(request):
    pop_post = Post.objects.all().order_by('-view')[:4]
    res_post = Post.objects.all().order_by('-date')[:4]
    cat = BlogCategory.objects.all()
    
    data = None
    totalResult = 0
    resfor=None
    if(request.GET.get("cat")):
        resfor = request.GET.get("cat")
        catid = BlogCategory.objects.filter(cat=resfor).first()
        if catid:
            data = Post.objects.filter(cat = catid.id,ready=True).order_by('-date')
            totalResult = Post.objects.filter(cat = catid.id,ready=True).count()
        else:
            data = Post.objects.none()
            totalResult = 0
        
        # name__unaccent__lower__trigram_similar
    elif(request.GET.get("srckey")):
        resfor = request.GET.get("srckey")
        
        if len(resfor)>20:
            data = Post.objects.none()
            totalResult = 0
        else:
            resTitle = Post.objects.filter(title__icontains=resfor,ready=True)
            resTag = Post.objects.filter(tag__icontains=resfor,ready=True)
            # resuser = Post.objects.filter(user__icontains=resfor)
            data = resTitle.union(resTag).order_by('-date')
            totalResult = data.count()

        
    else:
        HttpResponse("Invalid Key Entered error57nk 404")
    
    paginator = Paginator(data, 10, orphans=2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {"post":page_obj,"cat":cat,"ppost":pop_post,"resfor":resfor,"rpost":res_post,"rcount":totalResult}
    return render(request,"blog/search-result.html",context)
    
    


#-------------------------- Start: Blog-Post View ---------------------------------------------
@login_required(login_url='login')
def uploadPost(request):
    if request.method == 'POST':
        bform = PostForm(request.POST, request.FILES)
        
        if bform.is_valid():
            user = request.user
            if getPostData(user, bform):
                messages.success(request,"Post Uploaded Successful", fail_silently=True)
                return redirect('/author/' + str(request.user))
            else:
                messages.error(request,"Post Uploaded Fail", fail_silently=True)
                return HttpResponse("Data Not Saved")                       

        else:
            return HttpResponse("Form Error57nk")


    elif request.method == 'GET':
        blogForm = PostForm(initial={'user':request.user})
       
        context={"form":blogForm}  
        return render(request,"blog/upload-post.html",context)

def getPostData(user, bform):
    post_ready = False
    title = bform.cleaned_data.get('title')
    cat = bform.cleaned_data.get('cat')
    thumb = bform.cleaned_data.get('thumb')
    banner = bform.cleaned_data.get('banner')
    desc = bform.cleaned_data.get('desc')
    content = bform.cleaned_data.get('content')
    tag = bform.cleaned_data.get('tag')
    media = bform.cleaned_data.get('media')
    if(user.userprofile.verifyed):
        post_ready = True

    if(media):
        obj = Post.objects.create(
            user=user,
            title = title,
            thumb = thumb,
            banner=banner,
            content=content,
            cat=cat,
            desc=desc,
            tag=tag,
            media=media,
            ready=post_ready,
            pic1 =bform.cleaned_data.get('pic1'),
            pic2 =bform.cleaned_data.get('pic2'),
            pic3 =bform.cleaned_data.get('pic3'),
            pic4 =bform.cleaned_data.get('pic4'),
            pic5 =bform.cleaned_data.get('pic5')
        )

    else:
        obj = Post.objects.create(
            user=user,
            title = title,
            thumb = thumb,
            banner=banner,
            desc=desc,
            content=content,
            cat=cat,
            tag=tag,
            ready=post_ready,
            media=media,
        )
    try:
        obj.save()
        return True
        
    except:
        return False   


#-------------------------- Start: Blog-Post View ---------------------------------------------






#-------------------------- Start: User View ---------------------------------------------


def userprofile(request):
    return redirect('/author/' + str(request.user))


@login_required(login_url='home')
def logOutUser(request):
    logout(request)
    return redirect('/login/')


def loginUser(request):
    # if request.user == 'AnonymousUser':
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request,username = username,password = password)

                if user is not None:
                    login(request, user)
                    return redirect('profile')
                else:
                    messages.info(request,"Username/Password did not matched")
                    return redirect('login')
                    
        
        
        else:
            form = LoginForm()
            return render(request, 'blog/login.html',{'form':form})
    # else:
        # return redirect('profile')


def userReg(request):
    
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            cuser = form.cleaned_data.get('username')
            messages.success(request,"Account created for '" + cuser + "'", fail_silently=True)
            return redirect(loginUser)
        else:
            messages.error(request,"Form Error", fail_silently=False)
            # return redirect('register')
            return render(request,'blog/registration.html',context)
    else:
        form = UserRegForm()
        context = {"form":form}
        return render(request,'blog/registration.html',context)
    

@login_required(login_url='login')
def updateUser(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance = request.user.userprofile)
     
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Profile Updated Successful", fail_silently=True)
            return redirect('profile')
        else:
            messages.error(request,"Profile Update Fail", fail_silently=True)            
            return redirect('update-profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = UserProfileForm(initial={"userName":request.user.id},instance = request.user.userprofile)
        pop_post = Post.objects.filter(ready=True).order_by('-view')[:4]
        res_post = Post.objects.filter(ready=True).order_by('-date')[:4]
       
        cat = BlogCategory.objects.all()
        context = {"cat":cat,"ppost":pop_post,"rpost":res_post,'uform':u_form,'form':p_form}
        return render(request, 'blog/user_temp/user-update.html',context)


#--------------------------End: User View ---------------------------------------------


 

#testing
class PostV(ListView):
    # user = request.get.user
    # model = Post
    #coustom querry set querry set
    queryset = Post.objects.filter(ready=True)
    template_name ='blog/listposttest.html'
    context_object_name= 'nk'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PostV, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data--nk'
        return context




# _____________________________API_____________________________________


@api_view(['GET'])
def postApiList(request):
    post = Post.objects.filter(ready=True).order_by('-date')
    serial = PostSerializers(post, many=True)
    return Response(serial.data)



