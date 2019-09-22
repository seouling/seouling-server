from django.contrib import admin
from api.models import Plan, Spot, SpotPicture, User, Schedule, Comment, Visit, SpotTag

# Register your models here.
admin.site.register(Plan)
admin.site.register(Spot)
admin.site.register(Schedule)
admin.site.register(SpotPicture)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Visit)
admin.site.register(SpotTag)
