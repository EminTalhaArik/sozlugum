from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class DictionaryCategory(models.Model):
    name = models.CharField(max_length=150)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Dictionary Categories'
        verbose_name = 'Dictionary Category'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Dictionary(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.ImageField(
        upload_to='dictionary-icons/', null=True, blank=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True)

    created_by = models.ForeignKey(
        User, related_name='dictionary_created_by', on_delete=models.CASCADE)
    category = models.ManyToManyField(
        DictionaryCategory, related_name='dictionary_category')

    class Meta:
        verbose_name_plural = 'Dictionaries'
        verbose_name = 'Dictionary'
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Dictionary, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class TermCategory(models.Model):
    name = models.CharField(max_length=150)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dictionary = models.ForeignKey(
        Dictionary, related_name='term_category_dictionary', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Term Categories'
        verbose_name = 'Term Category'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Term(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.ImageField(upload_to='term-icons/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_star_term = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    dictionary = models.ForeignKey(
        Dictionary, related_name='term_dictionary', on_delete=models.CASCADE)
    category = models.ForeignKey(
        TermCategory, related_name='term_category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Terms'
        verbose_name = 'Term'
        ordering = ('name',)

    def __str__(self):
        return self.name
