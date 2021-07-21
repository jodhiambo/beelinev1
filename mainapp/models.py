from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
from django.utils import timezone
import datetime
from multiselectfield import MultiSelectField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
STATUS = (
    ('Open', 'Open'),
    ('Coming Soon', 'Coming Soon'),
    ('Archived', 'Archived'),
    ('Rolling', 'Rolling')
)

class ChallengeTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ChallengeAudience(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Challenges(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    offered_by = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media_pics/', blank=True, default='default-banner.jpg')
    challenge_summary = models.CharField(max_length=250, default='')
    description = RichTextUploadingField()
    external_website_url = models.CharField(max_length=150, default="")
    participate_link = models.CharField(max_length=200, default="")
    targeted_audience = models.ManyToManyField(ChallengeAudience)
    favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="fav_posts", blank=True, editable=False)
    tags = models.ManyToManyField(ChallengeTag)
    who_can_participate = RichTextUploadingField()
    how_to_participate = RichTextUploadingField()
    prize = models.CharField(max_length=150, help_text="Include the currency and amount in this field")
    additional_information = RichTextUploadingField()
    point_of_contact = models.TextField()
    status = models.CharField(choices=STATUS, max_length=200, default='Open')
    date_posted = models.DateTimeField(default=timezone.now, db_index=True)
    open_until = models.DateTimeField(null=True, blank=True, db_index=True)
    


    class Meta:
        verbose_name = 'challenge'
        verbose_name_plural = 'challenges'

    def get_absolute_url(self):
        return f'detail/{self.id}/{self.slug}/'

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Challenges)
def my_handler(sender, instance, **kwargs):
    instance.diff = instance.open_until - instance.date_posted


class Preapproved_challenge(models.Model):
    goal = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    external_url = models.CharField(max_length=150, default="")
    length = models.CharField(max_length=150)
    short_description = models.TextField()
    steps_to_complete = models.TextField()
    why = models.TextField(blank=True, null=True)
    tips = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(ChallengeTag)

    def __str__(self):
        return self.name
