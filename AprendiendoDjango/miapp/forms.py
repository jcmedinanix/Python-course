#from random import choices
from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title=forms.CharField(
        label="Titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Mete el Titulo',
                'class':'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El Titulo es demasiado Corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$','El titulo Contiene caracteres extraños','invalid_title')
        ]

    )

    content=forms.CharField(
        label="Contenido",
        widget=forms.Textarea(
            attrs={
                'placeholder':'Mete el Contenido1',
                'class':'content_form_article'
            }
        )
    )

    content.widget.attrs.update({
         'placeholder':'Mete el Contenido',
                'class':'content_form_article'
    })

    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public=forms.TypedChoiceField(
        label="Publicado?",
        choices=public_options
    )