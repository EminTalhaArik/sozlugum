from django.contrib import admin
from .models import Dictionary, DictionaryCategory, Term, TermCategory


@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'is_verified',)

    list_editable = ('is_active', 'is_verified',)

    list_display = ('name', 'description', 'is_active', 'is_verified')
    fields = ['name', 'description', 'icon', 'is_verified',
              'is_active', 'created_by', 'category', 'slug',]

    readonly_fields = ('slug',)


@admin.register(DictionaryCategory)
class DictionaryCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('is_active',)

    list_editable = ('is_active',)

    list_display = ('name', 'is_active')
    fields = ['name', 'is_active']


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'is_star_term')

    list_editable = ('is_active',)

    list_display = ('name', 'description', 'is_active',
                    'dictionary', 'category')
    fields = ['name', 'description', 'icon',
              'is_active', 'is_star_term', 'dictionary', 'category']


@admin.register(TermCategory)
class TermCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('is_active',)

    list_editable = ('is_active',)

    list_display = ('name', 'is_active', 'dictionary')
    fields = ['name', 'is_active', 'dictionary']
