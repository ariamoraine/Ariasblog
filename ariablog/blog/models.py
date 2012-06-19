from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max_length=30)
	body = models.CharField(max_length=500)
	date = models.DateField()

	@models.permalink
	def get_absolute_url(self):
		return ('ariablog.views.postpage', [str(self.id)])

	@models.permalink
	def get_edit_url(self):
		return ('ariablog.editpostlist', [str(self.id)])

	def __unicode__(self):
		return u'Title: %s' %(self.title)