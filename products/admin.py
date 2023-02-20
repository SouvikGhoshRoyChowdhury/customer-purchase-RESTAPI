from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin Class To Register Category Model And Filter Fields To Show In Django Admin
    """

    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ["make_unavailable"]
    list_display = ["name", "category", "stock", "price", "available"]
    list_editable = ["category", "available", "stock", "price"]
    list_filter = ["available", "category", "created"]
    preserve_filters = True
    search_fields = ["name"]

    @admin.action(description="Mark selected products as unavailable")
    def make_unavailable(self, request, queryset):
        updated = queryset.update(available=False)
        self.message_user(
            request,
            ngettext(
                f"{updated} product has been marked as unavailable",
                f"{updated} products have been marked as unavailable",
                updated,
            ),
            messages.SUCCESS,
        )
