from django.contrib import admin
from salina.content.models import *

# register the appropriate models with the admin
admin.site.register(Audio)
admin.site.register(NotesDoc)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Series)