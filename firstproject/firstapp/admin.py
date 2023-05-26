from django.contrib import admin
from firstapp.models import First

# Register your models here.
class FirstAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','phoneno','address']

admin.site.register(First,FirstAdmin)