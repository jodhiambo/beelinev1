from django.contrib import admin
from .models import Challenges, ChallengeAudience, Preapproved_challenge, ChallengeTag
from .forms import ChallengesModelForm

class ChallengesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']
    fieldsets = (
        ('', {
            'fields': ('title', 'slug', 'offered_by',
            'image', 'challenge_summary', 'description',
            'external_website_url', 'participate_link',
            'targeted_audience', 'tags', 'who_can_participate',
            'how_to_participate', 'prize', 'additional_information',
            'point_of_contact','status', 'date_posted',),
            'classes': ('predefined',)
        }),
        (None, {
            'fields': ('open_until',),
            'classes': ('abcdefg')
        })
    )
    form = ChallengesModelForm
    class Media:
        js = ('mainapp/js/base.js',)

admin.site.site_header = "Research Administration"
admin.site.site_title = "Research"

admin.site.register(Challenges, ChallengesAdmin)
admin.site.register(ChallengeAudience)
admin.site.register(Preapproved_challenge)
admin.site.register(ChallengeTag)
