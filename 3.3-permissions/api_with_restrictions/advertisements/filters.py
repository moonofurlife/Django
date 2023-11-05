from django_filters import rest_framework as filters, DateFromToRangeFilter, CharFilter
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    status = CharFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']

