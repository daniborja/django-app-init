from django.contrib import admin

from .models import Task


# ### Agregar attributes del Model q no se ven en el Django Admin
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", ) # solo d lectura en el admin

# ### Register your MODELS here.
admin.site.register(Task, TaskAdmin)

