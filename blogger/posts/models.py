from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

# Create your models here.

#def upload_location(instance, filename):
#	return "%s/%s" %(instance.id, filename)

class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		return super (PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())
		

class  Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")#upload_to=upload_location, 
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	objects = PostManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		#return "/post/%s/" %(self.id)
		return reverse("post:detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ['-timestamp','-updated']


#def create_slug(instance, new_slug=None):


def pre_save_post_reciever(sender, instance, *args, **kwargs):
	slug=instance.title
	while 1:
		slug = slugify(slug)
		exit = Post.objects.filter(slug=slug).order_by('-id')
		exists = exit.exists()
		if exists:
			slug = "%s-%s" %(slug, exit.first().id)
		else:
			break
	instance.slug = slug

pre_save.connect(pre_save_post_reciever, sender=Post)