from django.contrib import admin
from .models import Sports,Players,Bookings,Matches



@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
    list_display=('name','category')
    search_fields=('name',)

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display=('name','age','sport')
    list_filter=('sport',)
    search_fields=('name',)

@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    list_display=('sport','date','venue','teama','teamb','score')
    list_filter=('sport','date')
    search_fields=('teama','teamb')

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display=('bookingdate','username','match')
    list_filter=('bookingdate',)
    search_fields=('username',)


