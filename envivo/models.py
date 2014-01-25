from django.db import models

# Create your models here.
class Envivo(models.Model):
	titulo = models.CharField(max_length=200)
	url = models.TextField()
	vivo = models.BooleanField()

	def __unicode__(self):
		return self.titulo

	class Meta:
		verbose_name=u'En vivo'
		verbose_name_plural=u'En vivo'