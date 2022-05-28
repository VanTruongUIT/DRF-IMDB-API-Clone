from django.contrib import admin
from movies.models import (
    WatchList, 
    StreamPlatform, 
    Review
)

class WatchListAdmin(admin.ModelAdmin):
    pass 


class StreamPlatformAdmin(admin.ModelAdmin):
    pass 

class ReviewAdmin(admin.ModelAdmin):
    pass 


admin.site.register(WatchList, WatchListAdmin)
admin.site.register(StreamPlatform, StreamPlatformAdmin)
admin.site.register(Review, ReviewAdmin)