from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.views.generic import View

from john.models import Thread, Post, UserProfileJohn, Player, PostForm

# Create your views here.
# OK 
def main_page(request):
    threads = Thread.objects.all()
    context = {
        'threads' : threads, 
    }
    return render(request, 'john/main.html', context) 

class ThreadView(View):
    post_form = PostForm
    def get(self, request, thread_id):
        posts = Thread.objects.get(id = thread_id).post_set.all()
        form = self.post_form
        in_thread = _get_player(request.user, thread_id)
        context = {
            'in_thread' : in_thread,
            'posts' : posts,
            'self_id' : thread_id,
            'post_form' : form, 
            'active' : Thread.objects.get(id = thread_id).active_player,
        }
        return render(request, 'john/thread.html', context)
    def post(self, request, thread_id):
        #branching to other actions
        #wait, wait, shouldn't this be other functions in the class?!
        if 'action_reply' in request.POST:
            print 'action'
            url = '/john/' + str(thread_id) + '/longreply/'
            print url
            return HttpResponse('action time!')
            #return redirect(url)
        if 'long_reply' in request.POST:
            print 'long'
            url = '/john/' + str(thread_id) + '/longreply/'
            return HttpResponse('longform reply')
            #return redirect(url)
        in_thread = _get_player(request.user, thread_id)
        posts = Thread.objects.get(id = thread_id).post_set.all()
        form = self.post_form(request.POST)
        if form.is_valid():
            me = _get_player(request.user, thread_id)
            if me == False:
                return HttpResponse('you done goofed, ' + str(request.user))
            form.make_post(thread_id, me)

        context = {
            'in_thread' : in_thread,
            'posts' : posts,
            'self_id' : thread_id,
            'post_form' : form,
            'active' : Thread.objects.get(id = thread_id).active_player,
        }
        return render(request, 'john/thread.html', context)       


#oh yeah, this name isn't confusing *at all*
def post(request, post_id):
    return HttpResponse('post placeholder')



#helper to get player based on intersection of current user and thread
#returns false if user not in current thread
def _get_player(user, thread_id):
    try:
        up = UserProfileJohn.objects.get(base_user__username = user)
        player = up.player_set.get(game__id = thread_id)
    except:
        return False
    return player


