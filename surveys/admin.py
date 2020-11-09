from django.contrib import admin

# Register your models here.
from .models import Post,PostAdmin
from .models import NewUser


admin.site.register(Post,PostAdmin)
admin.site.register(NewUser)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    


 