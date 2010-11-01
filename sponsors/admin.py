from django.contrib import admin
from sponsors.models import *

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'aggregate_type', 'rank')
    prepopulated_fields = {"slug": ("name",),}
    list_editable = ('rank',)

class SponsorshipTypeAdmin(admin.ModelAdmin):
    list_display = ('singular', 'rank')

admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(SponsorshipType, SponsorshipTypeAdmin)
