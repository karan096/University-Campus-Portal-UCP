"""
Models file for Discussion App

consists of the model definitions for the discussion app
"""

from django.db import models
from django.utils import timezone

from UCP.functions import get_time_elapsed_string, get_file_size_string


class Tag(models.Model):
    """
    Tags for discussions , news , events and schedules.
    """
    name = models.CharField(null=True, max_length=100)
    
    def __unicode__(self):
        return self.name


class DiscussionThread(models.Model):
    """
    Discussion Thread model, a thread can have multiple replies or comments.
    """
    title = models.CharField( max_length=100)
    description = models.CharField( max_length=1000)
    posted_by = models.ForeignKey("login.UserProfile", null=True, blank=True)
    posted_at = models.DateTimeField(default=timezone.now)
    no_of_replies = models.IntegerField(blank=True, null=True, default=0)
    no_of_views = models.IntegerField(blank=True, null=True, default=0)
    last_reply = models.ForeignKey("Reply", related_name="last_reply", null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    subscribed = models.ManyToManyField("login.UserProfile", related_name="subscribed")
    
    class Meta:
        ordering = ['-posted_at']
    
    def time_elapsed(self):
        return get_time_elapsed_string(self.posted_at)
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return self.title


class Reply(models.Model):
    """
    Model for comments on a discussion thread
    """
    thread = models.ForeignKey(DiscussionThread)
    posted_by = models.ForeignKey("login.UserProfile", null=True, blank=True)
    posted_at = models.DateTimeField(default=timezone.now)
    text = models.CharField(default="", max_length="1000")
    
    class Meta:
        ordering = ['-posted_at']
    
    def time_elapsed(self):
        return get_time_elapsed_string(self.posted_at)
    


class Attachment(models.Model):
    """
    Model for file attachements on a reply to a discussion thread
    """
    name = models.CharField(blank=True ,null=True, max_length=100)
    reply = models.ForeignKey(Reply, related_name="attachments")
    uploaded_file = models.ImageField(upload_to="user-attachments")
    size = models.FloatField(default=0, blank=True)
    
    def size_in_kb(self):
        return get_file_size_string(self.size)
    
    def save(self, *args, **kwargs):
        self.name = self.uploaded_file.name
        self.size = self.uploaded_file.size
        super(Attachment, self).save(*args, **kwargs)
        
    
    
    
