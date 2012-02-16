from worktime.models import Employee, Time
from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
    fields = ['fname', 'lname']
    list_display = ('fname', 'lname')

class TimeAdmin(admin.ModelAdmin):
    fields = ['emp','start','end']
    list_display = ('emp','start','end')
    list_filter = ['start']
    #search_fields = ['emp']
    date_hierarchy = 'start'

admin.site.register(Employee,EmployeeAdmin)

admin.site.register(Time,TimeAdmin)
