from django.db import models

class Party(models.Model):
	name = models.CharField(max_length=128,unique=True)
	def __unicode__(self):
		return self.name

class MSP(models.Model):
	name = models.CharField(max_length=128)
	constituency = models.CharField(max_length=128)
	party = models.ForeignKey(Party)
	url = models.CharField(max_length=128)
	notes = models.CharField(max_length=1024)
	def __unicode__(self):
		return self.name

