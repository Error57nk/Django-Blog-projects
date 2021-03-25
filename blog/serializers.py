from rest_framework import serializers
from .models import Post, BlogCategory

class PostSerializers(serializers.ModelSerializer):
  user = serializers.CharField(source='userName', read_only=True)
  cat = serializers.CharField(source='catName', read_only=True)
  # pic1 = serializers.ImageField(source='img1.url', read_only=True)
  class Meta:
    model = Post
    # fields = '__all__'
    fields = ['id','user','title','desc','slug','thumb','banner','date','cat','view','tag']
    # exclude = ['feature','ready',]
   