from django.contrib import admin

from app.models import Hero, Attribute, Role, HeroRoles, Aspects, Skills, News


# Register your models here.
class HeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class HeroRolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'hero', 'role')


class AspectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Hero, HeroAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(HeroRoles, HeroRolesAdmin)
admin.site.register(Aspects, AspectsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(News, NewsAdmin)
