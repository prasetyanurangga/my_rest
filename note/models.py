from django.db import models

# Create your models here.
class NoteModel(models.Model):
	"""docstring for NoteModel"""
	title = models.CharField(max_length=100)
	body = models.TextField()
		