    
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import *
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('User Profile created!')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            #create the user profile if does not exist:
            print('User Profile does not exist, creating one...')
        print('User Profile is Updated!')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is about to be saved!')
post_save.connect(post_save_create_profile_receiver, sender=User)