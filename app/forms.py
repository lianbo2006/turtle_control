from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):   #类似与把UserCreationForm模块载入重新编写一下
	class Meta:
		model = User
		fields = ('username','email')  #UserCreationForm类里面fields里面默认只有username，加上email就可以在表单中显示email
