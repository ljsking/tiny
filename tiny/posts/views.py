from django.template import RequestContext
from django.shortcuts import render_to_response
from posts.models import Post
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

import facebook

import datetime

def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('posts/index.html', {
            'latest_post_list': latest_post_list,
        }, context_instance=RequestContext(request))

@login_required(login_url='/login/facebook/')
def post(request):
    msg = request.GET['message']
    email = request.user.email
    p = Post(message=msg, email=email, pub_date=datetime.datetime.now())
    p.save()
    '''
    sa = request.user.social_auth.get()
    token = sa.extra_data['access_token']
    graph = facebook.GraphAPI(token)
    graph.put_object('me','feed',message=msg)
    '''
    
    return HttpResponseRedirect(reverse('posts.views.index'))
    
@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {'version': version,
           'last_login': request.session.get('social_auth_last_login_backend')}
    return render_to_response('done.html', ctx, RequestContext(request))
    
def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
    
def error(request):
    """Error view"""
    messages = get_messages(request)
    return render_to_response('error.html', {'version': version,
                                             'messages': messages},
                              RequestContext(request))