from django.core.management.base import BaseCommand
from django.utils import timezone
from mainapp.models import Challenges


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        now = timezone.now()
        for challenge in Challenges.objects.all().iterator():
            if challenge.open_until < now:
                challenge.status = 'Archived'
                challenge.save()
