from email import contentmanager
from random import choices
from django import forms

class FormArticle(forms.Form):

    title=forms.CharField(
        label="Titulo",
        max_length=40,
        required=False

    )

    content=forms.CharField(
        label="Contenido",
        widget=forms.Textarea
    )

    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public=forms.TypedChoiceField(
        label="Publicado?",
        choices=public_options
    )