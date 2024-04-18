"""This module defines a Django form class called TestForm, which is used to
create and handle forms for the Post
model."""
from django import forms
from django_editorjs_fields import EditorJsWidget
from .models import Post


class TestForm(forms.ModelForm):
    """TestForm (forms.ModelForm): A subclass of Django's ModelForm class,
     customized for the Post model.
     - Meta (nested class):
     Contains metadata options for the TestForm class, including:
     - model: Specifies the model associated with the form (Post).
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
            model (Post): The model associated with the form.
            widgets (dict): Custom widgets for form fields.
        """
        model = Post
        exclude = []
        widgets = {
            'body_editorjs': EditorJsWidget(config={'minHeight': 100}),
            'body_editorjs_text': EditorJsWidget(plugins=["@editorjs/image", "@editorjs/header"])
        }
