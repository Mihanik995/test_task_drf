from django.contrib import admin

from distribution_network.models import Product, DistributionNod


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_date')


@admin.action(description="Write off debt from selected providers")
def write_off_dept(modeladmin, request, queryset):
    queryset.update(dept=0)


@admin.register(DistributionNod)
class DistribNodAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'country', 'city', 'street', 'building',
                    'dept', 'creation_datetime')
    filter_horizontal = ('products',)
    actions = [write_off_dept]
    search_fields = ('city',)
