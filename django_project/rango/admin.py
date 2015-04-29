from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class PageInline(admin.TabularInline): # a page can be added by admin when category is selected NOTE: can also use admin.StackedInline
    model = Page
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	fieldsets = [
        (None,               {'fields': ['name']}),
        ('Other information', {'fields': ['likes','views','slug'],'classes':['collapse']})]
        inlines = [PageInline]

class PageAdmin(admin.ModelAdmin):
	 list_display = ('title', 'views','url','category')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Page, PageAdmin)