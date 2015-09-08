from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from .models import Article
# Create your views here.

def detail(request, id):
    post = Article.objects.get(id=str(id))
    return render_to_response('post.html', {'post':post})

def index(request):
    post_list = Article.objects.all()
    context = {'post_list':post_list, }
    return render_to_response('index.html', context)
   # return HttpResponse(post)
    #return HttpResponse("title=%s, category=%s, date_time=%s, content= %s" %(post.title, post.category, post.date_time, post.content))

def archieve(request):
    try:
        post_list=Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('archieve.html', {'post_list':post_list,})

def aboutme(request):
    return render_to_response('aboutme.html')

def search_tag(request, tag=None):
    if len(tag) == 0:
        post_list = Article.objects.all()
    else:
        try:
            post_list = Article.objects.filter(category_iexact=tag)
        except Article.DoesNotExist:
            raise Http404
    return render_to_response('tag.html', {'post_list':post_list,})

'''def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))

    except Article.DoesNotExist:
        raise Http404
    name = 'sasasas'
    context = {'post':post,'name':name}
    #return  HttpResponse(post)
    return render_to_response('post.html', context)
'''