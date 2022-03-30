from django.contrib import admin

from backend.base.models import Userlist, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        # 'lists',
    )


class ItemsInline(admin.TabularInline):
    model = Item
    extra = 0


class ListsAdmin(admin.ModelAdmin):
    inlines = (ItemsInline,)
    list_display = (
        '__str__',
        'get_user_name',
    )

    @admin.display(description='Usuário', ordering='user__username')
    def get_user_name(self, obj):
        return obj.user


class ListsInline(admin.TabularInline):
    model = Userlist


class UsuaryAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )


admin.site.register(Userlist, ListsAdmin)
admin.site.register(Item, ItemAdmin)
