from django.contrib import admin

from backend.base.models import Lists, Item, Usuary


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'lists',
    )


class ItemsInline(admin.TabularInline):
    model = Item
    extra = 0


class ListsAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    inlines = (ItemsInline,)


class ListsInline(admin.TabularInline):
    model = Lists

    def has_add_permission(self, request, obj=None):
        return False


class UsuaryAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    inlines = (ListsInline,)



admin.site.register(Lists, ListsAdmin)
admin.site.register(Usuary, UsuaryAdmin)
admin.site.register(Item, ItemAdmin)
