from django.contrib import admin
from .models import JobCircular
# Register your models here.

from .models import *

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(Followers)
admin.site.register(JobCircular)

