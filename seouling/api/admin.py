from django.contrib import admin
from api.models import Plan, Spot, SpotPicture, User, Schedule, Tag, TagItem, Comment, Visit

# Register your models here.
admin.site.register(Plan)
admin.site.register(Spot)
admin.site.register(Schedule)
admin.site.register(SpotPicture)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(TagItem)
admin.site.register(Comment)
admin.site.register(Visit)
