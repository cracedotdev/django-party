from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from party.models import CustomUser, Party, Guest, Gift


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    pass

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
