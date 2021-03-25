from django import template
from django.utils.safestring import mark_safe
from blog.models import Post

register = template.Library()





@register.filter(name='blogconc')
def blogconc(value, post_id):
  tagFilter = {
    "#hd1":"</p><h4 class='bcon__subh1'>",
    "hd1#":"</h4><p class='bcon__con'>",
    "#hd2":"</p><h4 class='bcon__subh2'>",
    "hd2#":"</h4><p class='bcon__con'>",
    "#hd3":"</p><h4 class='bcon__subh3'>",
    "hd3#":"</h4><p class='bcon__con'>",
    "#cd1":"</p><pre><code>",
    "cd1#":"</code></pre><p class='bcon__con'>",
    "#uld1":"</p><ul class='bcon__ul_dot'>",
    "uld1#":"</ul><p class='bcon__con'>",
    "#uld2":"</p><ul class='bcon__ul_star'>",
    "uld2#":"</ul><p class='bcon__con'>",
    "#uld3":"</p><ul class='bcon__ul_check'>",
    "uld3#":"</ul><p class='bcon__con'>",
    "#lnkr":"</p><a href='",
    "#lnkn":"' class='bplink' target='_blank'>",
    "lnke#":"</a><p class='bcon__con'>",
    "*li":"<li>",
    "li*":"</li>",
    }
  escapeChar = {">":"&gt;","<":"&lt;"}
  newVal= value
  for ec in escapeChar.keys():
    newVal = newVal.replace(ec,escapeChar[ec])

  for i in tagFilter.keys():
    newVal = newVal.replace(i,tagFilter[i])

# Model Working for content Pictures
  post_pic = Post.objects.filter(id=int(post_id)).first()

  imgTag = ["#pic#1","#pic#2","#pic#3","#pic#4","#pic#5"]

  if post_pic.media:
    if newVal.find('#pic#1') != -1 and post_pic.pic1 != "":
      newVal = newVal.replace('#pic#1',
      '</p><img src="/media/{}" class="img-fluid" alt="{}"><p class="bcon__con">'.format(post_pic.pic1,post_pic.title))
    else:
      newVal = newVal.replace('#pic#1',"")


    if newVal.find('#pic#2') != -1 and post_pic.pic2 != "":
      newVal = newVal.replace('#pic#2',
      '</p><img src="/media/{}" class="img-fluid" alt="{}"><p class="bcon__con">'.format(post_pic.pic2,post_pic.title))
    else:
      newVal = newVal.replace('#pic#2',"")

    if newVal.find('#pic#3') != -1 and post_pic.pic3 != "":
      newVal = newVal.replace('#pic#3',
      '</p><img src="/media/{}" class="img-fluid" alt="{}"><p class="bcon__con">'.format(post_pic.pic3,post_pic.title))
    else:
      newVal = newVal.replace('#pic#3',"")

    if newVal.find('#pic#4') != -1 and post_pic.pic4 != "":
      newVal = newVal.replace('#pic#4',
      '</p><img src="/media/{}" class="img-fluid" alt="{}"><p class="bcon__con">'.format(post_pic.pic4,post_pic.title))
    else:
      newVal = newVal.replace('#pic#4',"")

    if newVal.find('#pic#5') != -1 and post_pic.pic5 != "":
      newVal = newVal.replace('#pic#5',
      '</p><img src="/media/{}" class="img-fluid" alt="{}"><p class="bcon__con">'.format(post_pic.pic5,post_pic.title))
    else:
      newVal = newVal.replace('#pic#5',"")

  else:
    for im in imgTag:
      newVal = newVal.replace(im," ")  

 

  
  return mark_safe(newVal)