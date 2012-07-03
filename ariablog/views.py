from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from blog.models import BlogPost 
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.simple import direct_to_template

def index(request): # is called from urls.py, gets the index.html renders it with the posts context. Requestcontext is for the user model.
	t = get_template('index.html')
	html = t.render(RequestContext(request,{'posts': BlogPost.objects.all()}))
	return HttpResponse(html)

def postpage(request, postid): #renders the post.html with the user data which will only work if its a request context
	t = get_template('post.html')
	html = t.render(RequestContext(request,{'post': BlogPost.objects.get(id = postid)}))
	return HttpResponse(html)

def newpost(request): # objects.create makes and saves a new database object 
	b = BlogPost.objects.create(title=request.POST["title"], body=request.POST["body"], date=datetime.date.today(), author=request.user)
	t = get_template('post.html')
	html = t.render(Context({'post': b, 'created': True})) # True is so a congrats message will show in post.html
	return HttpResponse(html)

def editpost(request, id):
	try:
		p = BlogPost.objects.get(id=id, author=request.user) 
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
	except BlogPost.DoesNotExist: #sends you back to previous page if you're not the author who created the post.
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', None))

def areyousure(request, id): #A confirmation page to double check the delete function
	t = get_template('areyousure.html')
	html = t.render(Context({'post': BlogPost.objects.get(id=id)}))
	return HttpResponse(html)

def deletepost(request, id):
	try:
		t = get_template('delete.html')
		BlogPost.objects.get(id=id, author=request.user).delete()
		html = t.render(Context())
		return HttpResponse(html)
	except BlogPost.DoesNotExist: #Redirects you if not the author.
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', None))

def signup(request):
	t = get_template('signup.html')
	html = t.render(Context())
	return HttpResponse(html)

def newuser(request):
	t = get_template('newuser.html')
	user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])#makes a user with the built in model.
	user.first_name=request.POST['firstname']
	user.last_name=request.POST['lastname']
	user.is_staff=False
	user.is_superuser=False
	user.save() #saves the first and last name which aren't included in the built in model. 
	html = t.render(Context({'user': user}))
	return HttpResponse(html)

def login_view(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password = request.POST['password']) #built in auth checks username and password 
	if user is None: #if the user isn't in the database redirected to signup page.
		t = get_template('signup.html')
		html = t.render(Context({'notuser': True}))
		return HttpResponse(html)
		#return direct_to_template(request, 'signup.html', 'notuser': True)
	elif not user.is_active:
		return direct_to_template(request, 'inactive_account.html')
	else:
		login(request, user)
		return HttpResponseRedirect('/')

def logout_view(request):
	t = get_template('logout.html')
	html = t.render(RequestContext(request))
	logout(request)
	return HttpResponse(html)
