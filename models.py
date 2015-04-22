from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms

# Create your models here.

##models
class Thread(models.Model):
    title = models.CharField(max_length = 100)
    game_master = models.ForeignKey("UserProfileJohn") 
    active_player = models.ForeignKey("Player", null = True)
    active = models.BooleanField(default = True)
    def __unicode__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread)
    created = models.DateTimeField(auto_now_add = True)
    creator = models.ForeignKey("Player")
    text = models.TextField(blank = False)
    
    def __unicode__(self):
        return unicode(self.creator) + " " + unicode(self.created) + " " + unicode(self.thread)
    
    class Meta:
        ordering = ['created']

#overarching profile, one per user
class UserProfileJohn(models.Model):
    base_user = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.base_user)

    #list of user owned players
    def list_games(self):
        return self.player_set.all()

#user representation in game, one per user per game, 1+ per user overall
class Player(models.Model):
    base_profile = models.ForeignKey(UserProfileJohn)
    name = models.CharField(max_length = 50)
    game = models.ForeignKey(Thread)
    willpower = models.IntegerField(default = 10)

    def __unicode__(self):
        return self.name

##forms

class PostForm(forms.Form):
    postbox = forms.CharField(widget = forms.Textarea, label = 'Enter text of post:')
    def make_post(self, thread_id, player):
        new_post = Post(thread = Thread.objects.get(id = thread_id), creator = player, text = self.cleaned_data['postbox'])
        new_post.save()
        return True

##magic signals
#they're magically delicious!

def user_profile_john_create(sender, instance, created, **kwargs):
    if created == True:
        u = UserProfileJohn()
        u.base_user = instance
        u.save()

post_save.connect(user_profile_john_create, sender = User)


