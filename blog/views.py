from django.shortcuts import render_to_response
from django.http import HttpResponse
import django
from .models import Article
# Create your views here.

def si(request, id):
    d = django.get_version()
    return HttpResponse('%s %s' %(d, id))

def detail(request):
    post_list = Article.objects.all()
    context = {'post_list':post_list, }
    return render_to_response('detail.html', context)
   # return HttpResponse(post)
    #return HttpResponse("title=%s, category=%s, date_time=%s, content= %s" %(post.title, post.category, post.date_time, post.content))