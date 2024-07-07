# myapp/filters.py
from django_filters import rest_framework as filters
from .models import Competition, Result, Club
from django.utils.timezone import now
from django.db.models import Q

class Filter_Upcoming_Competition(filters.FilterSet):
    upcoming = filters.BooleanFilter(method='filter_upcoming', label='Upcoming Competitions')
    ordering = filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('competition_category', 'competition_category'),
            ('start', 'start'),
            ('end', 'end'),
            ('competition_type__nickname', 'competition_type'),
        ),
    )

    class Meta:
        model = Competition
        fields = ['upcoming', 'competition_category', 'start', 'end']

    def filter_upcoming(self, queryset, name, value):
        if value:
            return queryset.filter(start__gte=now())
        return queryset

class Filter_Past_Competition(filters.FilterSet):
    past = filters.BooleanFilter(method='filter_past', label='Past Competitions')
    ordering = filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('competition_category', 'competition_category'),
            ('start', 'start'),
            ('end', 'end'),
            ('competition_type__nickname', 'competition_type'),
        ),
    )

    class Meta:
        model = Competition
        fields = ['past', 'competition_category', 'start', 'end']

    def filter_past(self, queryset, name, value):
        if value:
            return queryset.filter(start__lt=now())
        return queryset 


class Filter_Result_WeightClass_Age(filters.FilterSet):
    weight_class = filters.CharFilter(method='filter_weight_class')
    age_category = filters.CharFilter(method='filter_age_category')

    class Meta:
        model = Result
        fields = ['weight_class', 'age_category']

    def filter_weight_class(self, queryset, name, value):
        weight_classes = [wc.strip() for wc in value.split(',')]
        q_objects = Q()
        for wc in weight_classes:
            q_objects |= Q(weight_class__title__icontains=wc)
        return queryset.filter(q_objects)

    def filter_age_category(self, queryset, name, value):
        age_categories = [ac.strip() for ac in value.split(',')]
        q_objects = Q()
        for ac in age_categories:
            q_objects |= Q(age_category__title__icontains=ac)
        return queryset.filter(q_objects)

                                      
#Filter for results

class Filter_Ranking_Date_Age_Gender(filters.FilterSet):
    start_date = filters.DateFilter(field_name="group__competition__start", lookup_expr='gte')
    end_date = filters.DateFilter(field_name="group__competition__end", lookup_expr='lte')
    age_category = filters.CharFilter(field_name="age_category__title", lookup_expr='iexact')
    gender = filters.CharFilter(field_name="license_nr__person__gender", lookup_expr='iexact')

    discipline = filters.CharFilter(method='filter_discipline', label='Discipline')

    class Meta:
        model = Result
        fields = ['start_date', 'end_date', 'age_category', 'gender', 'discipline']

    def filter_discipline(self, queryset, name, value):
        if value.lower() == 'squat':
            queryset = queryset.filter(squat__gt=0)
            queryset = queryset.exclude(benchpress__gt=0, deadlift__gt=0)
        elif value.lower() == 'benchpress':
            queryset = queryset.filter(benchpress__gt=0)
            queryset = queryset.exclude(squat__gt=0, deadlift__gt=0)
        elif value.lower() == 'deadlift':
            queryset = queryset.filter(deadlift__gt=0)
            queryset = queryset.exclude(squat__gt=0, benchpress__gt=0)
        return queryset

#Filter för klubbar och distrikt

class Filter_Club_District_ClubName(filters.FilterSet):
    district_name = filters.CharFilter(field_name='district__district_name', lookup_expr='icontains')
    club_name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    order_by = filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('district__district_name', 'district_name'),
        )
    )

    class Meta:
        model = Club
        fields = ['district', 'name']