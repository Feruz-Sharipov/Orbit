from django.contrib import admin

from .models import About, Category,Portfolio,Services,Resume,HeppiClents,Contect

admin.site.register(About)
admin.site.register(Portfolio)
admin.site.register(Category)
admin.site.register(Services)
admin.site.register(Resume)
admin.site.register(HeppiClents)

class ContectAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "is_published")
    list_filter = ("is_published",)
    readonly_fields = ("create_at","updata_at")
    search_fields = ("first_name", "last_name")
admin.site.register(Contect)