from django.contrib import admin
from salina.content.models import *

class TagAdmin(admin.ModelAdmin):
    list_display = ('slug', 'label')
    list_editable = ('label',)

# register the appropriate models with the admin
admin.site.register(Audio)
admin.site.register(NotesDoc)
admin.site.register(Post)
admin.site.register(Tag, TagAdmin)
admin.site.register(Series)