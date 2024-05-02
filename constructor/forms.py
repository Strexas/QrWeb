"""This module defines a Django form class called PageForm, which is used to
create and handle forms for the Page
model."""
from django import forms
from django_editorjs_fields import EditorJsWidget
from profile.models import Page


class PageForm(forms.ModelForm):
    """PageForm (forms.ModelForm): A subclass of Django's ModelForm class,
     customized for the Page model.
     - Meta (nested class):
     Contains metadata options for the PageForm class, including:
     - model: Specifies the model associated with the form (Page).
     - exclude: Specifies which fields from the model should be excluded from the form.
     - widgets: Specifies custom widgets for form fields,
     where keys are field names and values are widget instances.
     - 'body_editorjs': Widget for the 'body_editorjs' field,
    utilizing the EditorJsWidget from django_editorjs_fields.
    - config: Custom configuration options for the
    EditorJsWidget, setting the minimum height of the editor to 100 pixels.
    - 'body_editorjs_text': Widget for the
    'body_editorjs_text' field, utilizing the EditorJsWidget from django_editorjs_fields.
    - plugins: Specifies the
    plugins to be used with the EditorJsWidget (e.g., '@editorjs/image', '@editorjs/header').
    """

    class Meta:  # pylint: disable=R0903
        """
        Metadata options for the TestForm class.

        Attributes:
            model (Page): The model associated with the form.
            widgets (dict): Custom widgets for form fields.
        """
        model = Page
        exclude: list[str] = []
        fields = ['title', 'content']
        widgets = {
            'body_editorjs': EditorJsWidget(config={'minHeight': 100}),
            'body_editorjs_text': EditorJsWidget(plugins=["@editorjs/image", "@editorjs/header"])
        }
