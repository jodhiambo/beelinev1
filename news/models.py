from django.db import models
from PIL import Image
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField



class News(models.Model):
    banner_image = models.ImageField(upload_to='media_pics/%Y/%m/%d', blank=True, default='default-banner.jpg')
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, max_length=250, db_index=True)
    summary = models.CharField(max_length=200)
    outsourced_news_link = models.CharField(max_length=200, blank=True, null=True, help_text=u"If you choose to enter outsourced news link (referencing news from another website), there's no need to type anything in the Body section")
    date_posted = models.DateField(default=timezone.now)
    body = RichTextUploadingField(blank=True, null=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def get_absolute_url(self):
        return f'news/{self.id}/{self.slug}'

    def __str__(self):
        return self.title + " " + str(self.date_posted)
