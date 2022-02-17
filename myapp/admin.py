from django.contrib import admin
from . models import Musician,Album

class Musicianadmin(admin.ModelAdmin):
    list_display=['first_name','last_name','instrument']
admin.site.register(Musician,Musicianadmin)

class Albumadmin(admin.ModelAdmin):
    list_display=["artist","name","release_date","num_stars"]
admin.site.register(Album,Albumadmin)
# Register your models here.
