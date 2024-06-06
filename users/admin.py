from django.contrib import admin

from users.models import User, Payment

# admin.site.register(User)
admin.site.register(Payment)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
