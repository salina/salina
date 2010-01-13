from django.db import models
from django.contrib.auth.models import User
from pybible.djangoforms import VerseField


class Classifier(models.Model):
    """Abstract base class for all grouping/classification classes below"""
    label = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True, blank = True, help_text = "This is used by code and may show up in URLs. Use lowercase letters, numbers, and the hyphen character (-) only.")
    def __unicode__(self):
        return self.label
    
    class Meta:
        abstract = True
        ordering = ['label'] #alphabetical order


class Scripture(models.Model):
    """Abstract base class for all objects that reference a Bible verse or passage"""
    start_verse = VerseField()
    end_verse = VerseField()
    
    class Meta:
        abstract = True


class Tag(Classifier):
    """Tags to be applied to all docs and FAQ"""


class Series(Classifier, Scripture):
    """Tags to be applied to all docs and FAQ"""


class ContentItem(Scripture):
    """Abstract base class for all grouping/classification classes below"""
    title = models.CharField(max_length = 200, verbose_name = "Headline", help_text = "Try to keep this fairly short and concise.")
    author = models.ForeignKey(User, blank=True, null=True, help_text = "Optional username of whoever created this or is featured in it")
    slug = models.SlugField(unique = True, blank = True, help_text = "This will be used in URLs. Must be unique. Use lowercase letters, numbers, and the hyphen character (-) only.")
    tags = models.ManyToManyField(Tag, blank = True)
    date = models.DateTimeField('Date', db_index = True, help_text = "Date the content was created.")
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return self.title
    
    class Meta:
        abstract = True
        ordering = ['-date'] # reverse chronological order


class NotesDoc(ContentItem):
    """A document containing notes from a sermon or other topic"""
    description = models.TextField(help_text = "This is displayed on the list page and in the RSS feed only.")
    content = models.TextField(help_text = "The body of the notes goes here. Markdown is supported.")


class Audio(ContentItem):
    """An audio recording with reference to actual data file on Archive.org"""
    description = models.TextField(help_text = "A brief description of the sermon/clip. Displayed on page with audio and in lists/RSS.")
    mp3 = models.URLField(help_text = "The full URL to the MP3 file (upload to Archive.org)")
    notes = models.ManyToManyField(NotesDoc, blank = True)


class Post(ContentItem):
    """A single blog post"""
    intro = models.TextField(help_text = "This is displayed on the list page and in the RSS feed. It is also displayed at the top of the post.")
    content = models.TextField(help_text = "This is the rest of the post. On the actual post page, this content will just flow right in after the intro. Markdown is supported")
    audio = models.ManyToManyField(Audio, blank = True)
    notes = models.ManyToManyField(NotesDoc, blank = True)