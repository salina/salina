from django.db import models
from django.contrib.auth.models import User

class Recording(models.Model):
    """An audio recording with reference to actual data file on Archive.org"""
    author = models.ForeignKey(User, blank=True, null=True, help_text = "Optional username of whoever was preaching or created the clip")
    title = models.CharField(max_length = 200, help_text = "What is the title of this sermon/clip")
    description = models.TextField(help_text = "A brief description of the sermon/clip")
    mp3 = models.URLField(help_text = "The full URL to the MP3 file (upload to Archive.org)")
    rec_date = models.DateTimeField('Date', db_index = True, help_text = "Date of the recording.")
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return self.title