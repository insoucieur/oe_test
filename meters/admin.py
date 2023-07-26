from django.contrib import admin
from meters.models.reading import Reading


class ReadingAdmin(admin.ModelAdmin):
    list_display = ('mpan', 'meter_id', 'register_id', 
                    'reading', 'reading_timestamp', 'filename')
    search_fields = ('mpan', 'meter_id')

admin.site.register(Reading, ReadingAdmin)