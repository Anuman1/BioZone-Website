from django.contrib import admin

from instrument.models import Instrument
from django.contrib import admin
# Register your models here.

from import_export.admin import ImportExportModelAdmin

class InstrumentAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug':('instrument_name',)}
    list_display = ('instrument_name', 'slug', 'category', 'institute',)    

admin.site.register(Instrument, InstrumentAdmin)