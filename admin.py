from django.contrib import admin

from john.models import Thread, Post, UserProfileJohn, Player
# Register your models here.

class ThreadAdmin(admin.ModelAdmin):
    fields = ['title', 'game_master', 'active_player']

class PostAdmin(admin.ModelAdmin):
    fields = ['thread', 'creator', 'text']

class UserProfileJohnAdmin(admin.ModelAdmin):
    fields = ['base_user']
class PlayerAdmin(admin.ModelAdmin):
    fields = ['base_profile', 'name', 'game', 'willpower']

admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin) 
admin.site.register(UserProfileJohn, UserProfileJohnAdmin)
admin.site.register(Player, PlayerAdmin)
