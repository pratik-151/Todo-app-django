from django.contrib import admin
from app.models import TODO
# Register your models here.

class TODOAdmin(admin.ModelAdmin):
    list_display = ("title", "user",)

admin.site.register(TODO,TODOAdmin)