from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from blog.models import BlogPost 
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.simple import direct_to_template

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

def signup(request):
	t = get_template('signup.html')
	html = t.render(Context())
	return HttpResponse(html)

def newuser(request):
	t = get_template('newuser.html')
	user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
	user.first_name=request.POST['firstname']
	user.last_name=request.POST['lastname']
	user.is_staff=False
	user.is_superuser=False
	user.save()
	html = t.render(Context({'user': user}))
	return HttpResponse(html)

def mylogin(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				if request.POST['next']:
					login=True
					return HttpResponseRedirect(request.POST['next'])
				else:
					login=True
					return HttpResponseRedirect('/')
			else:
				# disabled account
				return direct_to_template(request, 'inactive_account.html')
		else:
			# invalid login
			return direct_to_template(request, 'invalid_login.html')

def mylogout(request):
	logout(request)
	return direct_to_template(request, 'loggedout.html')
#create a signin.html
#make sign in link on main page
#make new post show when signed in 
#add user id to blog posts
#show username on blog posts
#only edit your own blog posts
