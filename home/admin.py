from django.contrib import admin
from .models import Blog,Team,Projects,Metrics,LibraryPictures,BoardMembers,OurWork
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted',)
    list_per_page = 10 
    
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','date_started','date_completed')
    list_per_page = 10



admin.site.register(Blog,BlogAdmin)
admin.site.register(Team)
admin.site.register(BoardMembers)
admin.site.register(Projects,ProjectAdmin)
admin.site.register(Metrics)
admin.site.register(LibraryPictures),
admin.site.register(OurWork)