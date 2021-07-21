from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from PIL import Image
from django.dispatch import receiver
from users.countries import COUNTRIES
from users.models import CustomUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)


AGE_RANGE = (
    # ('----', '----'),
    ('Below 18 Yrs', 'Below 18 Yrs'),
    ('18-35 Yrs', '18-35 Yrs'),
    ('Above 35 Yrs', 'Above 35 Yrs')
) 
# Create your models here.
class Profile(models.Model):
    # username = Nonee
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    nationality = models.CharField(choices=COUNTRIES, max_length=150)
    country_of_residence = models.CharField(choices=COUNTRIES, max_length=150)
    organization = models.CharField(max_length=50, default='')
    age_group = models.CharField(choices=AGE_RANGE, max_length=50, default='', blank=True, null=True)
    sex = models.CharField(choices=GENDER, max_length=200)
    consent_to_share_my_information = models.BooleanField(default=False)
    consent_to_view_my_bookmarks = models.BooleanField(default=False)
    # photo = ProcessedImageField(upload_to='profile_pics/',
    #                                 processors=[ResizeToFill(100,100)],
    #                                 format='JPEG',
    #                                 blank=True,
    #                                 default='default.jpg',
    #                                 options={'quality':60}
    #                                 )
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
