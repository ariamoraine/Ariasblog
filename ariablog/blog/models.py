from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
	title = models.CharField(max_length=30)
	body = models.CharField(max_length=500)
	date = models.DateField()
	author = models.ForeignKey(User)

	@models.permalink
	def get_absolute_url(self):
		return ('ariablog.views.postpage', [str(self.id)])

	@models.permalink
	def get_edit_url(self):
		return ('ariablog.editpostlist', [str(self.id)])

	def __unicode__(self):
		return u'Title: %s' %(self.title)