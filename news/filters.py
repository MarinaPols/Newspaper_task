from django.forms import DateInput

from django_filters import (FilterSet,
                            ModelChoiceFilter,
                            ModelMultipleChoiceFilter,
                            DateFilter,
                            CharFilter,
                            )

from .models import Author, Category


class PostFilter(FilterSet):
    date = DateFilter(
        field_name='dateCreation',
        lookup_expr='gte',
        label='Posted after',
        widget=DateInput(attrs={'type': 'date'})
    )
    title = CharFilter(
        lookup_expr='icontains',
        label='Include'
    )
    author = ModelChoiceFilter(
        queryset=Author.objects.all(),
        label='Author',
        empty_label='All'
    )
    date.field.error_messages = {'invalid': 'Enter date in format DD.MM.YYYY. Example: 31.12.2020'}
    date.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}
    # Этот вариант не самый удачный!
    # Category = ModelChoiceFilter(
    #     field_name='postCategory',
    #     queryset=Category.objects.all(),
    #     label='Категория',
    #     empty_label='Любая'
    # )
    Category = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
    )
   #class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       #model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       #fields = {
           # поиск по автору
           #'author',
           #'title',
           #'dateCreation',
           ##'rating',

       #}