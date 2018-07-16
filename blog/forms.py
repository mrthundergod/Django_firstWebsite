from django.forms import Modelform
from .models import Post

class PostForm(Modelform):
	class Meta:
		model = Post
		fields =('title', 'text',)