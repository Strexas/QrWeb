"""Module for Editor.js integration in Django.

This module provides fields and widgets for integrating Editor.js, a block-style editor
for rich content creation, into Django forms.

Attributes:
    __version__ (str): The version of the Editor.js integration module.

Usage:
- Import the fields and widgets provided by this module to use them in your Django forms.
- The '__version__' attribute can be used to access the version of this module.

Example:
    from .fields import EditorJsJSONField, EditorJsTextField
    from .widgets import EditorJsWidget

    __all__ = ("EditorJsTextField", "EditorJsJSONField", "EditorJsWidget", "__version__")
"""

__version__ = "0.2.7"

from .fields import EditorJsJSONField, EditorJsTextField
from .widgets import EditorJsWidget

__all__ = ("EditorJsTextField", "EditorJsJSONField", "EditorJsWidget", "__version__")
