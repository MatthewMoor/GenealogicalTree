from django.contrib import admin
from datatree.models import People, Relation
# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
    pass

class RelationAdmin(admin.ModelAdmin):
    pass

admin.site.register(People, PeopleAdmin)

from mptt.admin import MPTTModelAdmin

admin.site.register(Relation, MPTTModelAdmin)