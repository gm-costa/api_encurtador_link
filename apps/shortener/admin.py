from django.contrib import admin
from .models import Link, Click


class LinkAdmin(admin.ModelAdmin):
    list_display = ['redirect_link', 'token', 'create_at', 'expiration_time', 'max_uniques_cliques', 'active']

class ClickAdmin(admin.ModelAdmin):
    list_display = ['link', 'ip', 'create_at']

admin.site.register(Link, LinkAdmin)
admin.site.register(Click, ClickAdmin)
