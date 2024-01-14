
from django.contrib import admin
from django.contrib.sessions.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'expire_date', 'get_session_data')

    def get_session_data(self, obj):
        # Display a snippet of session data
        return str(obj.get_decoded())

    get_session_data.short_description = 'Session Data'
