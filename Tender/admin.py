from django.contrib import admin
from .models import Tender, User, Region


class UserAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'nameU', )
admin.site.register(User, UserAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'nameR', )
admin.site.register(Region, RegionAdmin)


@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
	list_display = (
		'id', 'numT', 'startsSumT', 'infoT',
        'delT', 'zhnvlpT', 'dateAddT',
        'dateActionT', 'dateDocT',
	)
	fields = [
		'userAddFK', 'regionFK', 'numT', 'startsSumT',
		('delT', 'zhnvlpT'),
		('dateAddT', 'dateActionT', 'dateDocT'),
		'infoT',
	]