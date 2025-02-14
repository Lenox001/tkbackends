from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
from .models import SafariPackage, Destination, SafariBooking, SafariAdventure, SafariItinerary

admin.site.site_header = "Safari Management Dashboard"
admin.site.site_title = " Admin page"
admin.site.index_title = "TK Safaris"


class SafariItineraryInline(admin.TabularInline):  
    model = SafariItinerary
    extra = 1  # Allows adding itinerary days directly inside SafariPackage


@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_overview_short', 'get_image_preview')
    search_fields = ('title', 'overview', 'full_description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SafariItineraryInline]

    def get_overview_short(self, obj):
        return obj.overview[:50] + "..." if len(obj.overview) > 50 else obj.overview
    get_overview_short.short_description = "Overview"

    def get_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;"/>', obj.image.url)
        return "No Image"
    get_image_preview.short_description = "Image Preview"


@admin.register(SafariItinerary)
class SafariItineraryAdmin(admin.ModelAdmin):
    list_display = ('safari_package', 'day_number', 'title')
    list_filter = ('safari_package',)
    ordering = ('safari_package', 'day_number')
    search_fields = ('safari_package__title', 'title')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_image_preview')
    prepopulated_fields = {'slug': ('title',)}

    def get_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;"/>', obj.image.url)
        return "No Image"
    get_image_preview.short_description = "Image Preview"


@admin.register(SafariBooking)
class SafariBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'destination', 'safari_type', 'time', 'submitted_at')
    list_filter = ('safari_type', 'time')
    search_fields = ('name', 'destination', 'phone_number')
    ordering = ('-submitted_at',)  # Show newest bookings first


@admin.register(SafariAdventure)
class SafariAdventureAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image_preview')
    search_fields = ('title', 'description')

    def get_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;"/>', obj.image.url)
        return "No Image"
    get_image_preview.short_description = "Image Preview"
