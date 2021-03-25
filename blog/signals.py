from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Profile Model
from . models import UserProfile

@receiver(post_save,sender=User)
def create_userprofile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(userName = instance)
    print('Profile Created')

post_save.connect(create_userprofile, sender = User)