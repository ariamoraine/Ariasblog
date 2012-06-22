from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from blog.models import BlogPost 
import datetime

def index(request):
	t = get_template('index.html')
	html = t.render(Context({'posts': BlogPost.objects.all()}))
	return HttpResponse(html)

def postpage(request, postid):
	t = get_template('post.html')
	html = t.render(Context({'post': BlogPost.objects.get(id = postid)}))
	return HttpResponse(html)

def newpost(request):
	b = BlogPost.objects.create(title=request.POST["title"], body=request.POST["body"], date=datetime.date.today())
	t = get_template('post.html')
	html = t.render(Context({'post': b, 'created': True}))
	return HttpResponse(html)

def editpost(request, id):
	p = BlogPost.objects.get(id=id)
	if request.method == 'GET':
		t = get_template('editpost.html')
		html = t.render(Context({'post': p}))
		return HttpResponse(html)
	elif request.method == 'POST':
		p.title = request.POST["title"]
		p.body = request.POST["body"]
		p.save()
		t = get_template('post.html')
		html = t.render(Context({'post': p, 'edited': True}))
		return HttpResponse(html)
		
def areyousure(request, id):
	t = get_template('areyousure.html')
	html = t.render(Context({'post': BlogPost.objects.get(id=id)}))
	return HttpResponse(html)

def deletepost(request, id):
	t = get_template('delete.html')
	BlogPost.objects.get(id=id).delete()
	html = t.render(Context())
	return HttpResponse(html)