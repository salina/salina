from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    # Django Admin
    (r'^admin/', include(admin.site.urls)),
    
    # Example:
    (r'^$', 'salina.content.views.home'),
    
)
