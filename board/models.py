import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

#User model for user registration
@python_2_unicode_compatible
class User(models.Model):
    name = models.CharField(max_length=128)
    reg_date = models.DateField()

    def __str__(self):
        return self.name

#study topics
@python_2_unicode_compatible
class Topic(models.Model):
    topic_name = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date created')
    member = models.ManyToManyField(User, through='Subscription')

    def __str__(self):
        return self.topic_name

# Study material submitted by users in a topic
#@python_2_unicode_compatible
class Resources(models.Model):
    #topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #title = models.CharField(max_length=250)
    #need links and names for study group resources
    pass

#intermediate model for resources
#@python_2_unicode_compatible
class Citation(models.Model):
    #topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #resource = models.ForeignKey(Resources, on_delete=models.CASCADE)
    pass

#User subscriptions to topics
#@python_2_unicode_compatible
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subscription_date = models.DateField()

# Create your models here.
