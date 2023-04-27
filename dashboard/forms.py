from django.forms import ModelForm
from core.models import Dictionary, DictionaryCategory, Term, TermCategory


class DictionaryForm(ModelForm):
    class Meta:
        model = Dictionary
        fields = "__all__"
        exclude = ["user", "slug"]


class DictionaryCategoryForm(ModelForm):
    class Meta:
        model = DictionaryCategory
        fields = "__all__"


class TermForm(ModelForm):
    class Meta:
        model = Term
        fields = "__all__"


class TermCategoryForm(ModelForm):
    class Meta:
        model = TermCategory
        fields = "__all__"
