from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from cloudinary.models import CloudinaryField
  

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='profile')
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
class Post(models.Model):
         id = models.UUIDField(primary_key=True,default=uuid.uuid4)
         user = models.CharField(max_length=100)
         image = CloudinaryField('image')
         caption = models.TextField()
         created_at = models.DateTimeField(default=datetime.now)
         no_of_likes = models.IntegerField(default=0)
         
class Meta:
        '''
        Class method to display images by date published
        '''
        ordering = ["-pk"]

def save_post(self):
        '''
        Method to save our images
        '''
        self.save()

def delete_post(self):
        '''
        Method to delete our images
        '''
        self.delete()
         
def __str__(self):
         return self.user
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
class Comment(models.Model):
    comment = models.TextField()
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user=models.ForeignKey(Profile,related_name='comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.comment
    class Meta:
        ordering=["-pk"]
 