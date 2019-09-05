from django.contrib import admin
from api.models import Plan, Spot, SpotPicture, User, Schedule

# Register your models here.
admin.site.register(Plan)
admin.site.register(Spot)
admin.site.register(Schedule)
admin.site.register(SpotPicture)
admin.site.register(User)
