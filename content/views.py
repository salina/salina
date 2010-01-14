from django.views.generic.simple import direct_to_template
from salina.content.models import Tag

def home(request):
    tags = Tag.objects.all()
    return direct_to_template(request, 'home.html', {
        'tags': tags,
    })