from django.contrib import admin
from datatree.models import Relation
# Register your models here.

class RelationAdmin(admin.ModelAdmin):
    pass

from mptt.admin import MPTTModelAdmin

admin.site.register(Relation, MPTTModelAdmin)