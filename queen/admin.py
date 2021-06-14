from django.contrib import admin
from .models import CANDIDATE,PARTY,ELECTION,AREA,VOTE,IMAGE

# Register your models here.
admin.site.register(CANDIDATE)
admin.site.register(PARTY)
admin.site.register(ELECTION)
admin.site.register(AREA)
admin.site.register(VOTE)
admin.site.register(IMAGE)