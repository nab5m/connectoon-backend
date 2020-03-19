from django.contrib import admin

from account.models import Role
from account.models import Account


class RoleAdmin(admin.ModelAdmin):
    pass


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name')


admin.site.register(Role, RoleAdmin)
admin.site.register(Account, AccountAdmin)
