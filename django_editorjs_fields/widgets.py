"""Custom widget for Editor.js."""

from django.core.serializers.json import DjangoJSONEncoder
from django.forms import Media, widgets
from django.forms.renderers import get_default_renderer
from django.utils.encoding import force_str
from django.utils.functional import Promise, cached_property
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from .config import CONFIG_TOOLS, PLUGINS, PLUGINS_KEYS, VERSION


class LazyEncoder(DjangoJSONEncoder):
    """Custom JSON encoder to handle Promise objects."""

    def default(self, o):
        """
        Serialize objects to a JSON format.

        Args:
            o: Object to be serialized.

        Returns:
            str: Serialized JSON string.
        """
        if isinstance(o, Promise):
            return force_str(o)
        return super().default(o)


# Instantiate the LazyEncoder
json_encode = LazyEncoder().encode


class EditorJsWidget(widgets.Textarea):
    """
    Custom widget for Editor.js integration.

    Args:
        plugins (list): List of plugins.
        tools (dict): Dictionary of tools.
        config (dict): Configuration options.
        **kwargs: Additional keyword arguments.
    """

    def __init__(self, plugins=None, tools=None, config=None, **kwargs):
        """Initialize the EditorJsWidget."""
        self.plugins = plugins
        self.tools = tools
        self.config = config

        # Fix "__init__() got an unexpected keyword argument 'widget'"
        widget = kwargs.pop('widget', None)
        if widget:
            self.plugins = widget.plugins
            self.tools = widget.tools
            self.config = widget.config

        super().__init__(**kwargs)

    def configuration(self):
        """
        Generate the configuration for the widget.

        Returns:
            dict: Configuration options.
        """
        tools = {}
        config = self.config or {}

        if self.plugins or self.tools:
            custom_tools = self.tools or {}
            # get name packages without version
            plugins = ['@'.join(p.split('@')[:2])
                       for p in self.plugins or PLUGINS]

            for plugin in plugins:
                plugin_key = PLUGINS_KEYS.get(plugin)

                if not plugin_key:
                    continue

                plugin_tools = custom_tools.get(
                    plugin_key) or CONFIG_TOOLS.get(plugin_key) or {}
                plugin_class = plugin_tools.get('class')

                if plugin_class:
                    tools[plugin_key] = custom_tools.get(
                        plugin_key, CONFIG_TOOLS.get(plugin_key)
                    )

                    tools[plugin_key]['class'] = plugin_class

                    custom_tools.pop(plugin_key, None)

            if custom_tools:
                tools.update(custom_tools)
        else:  # default
            tools.update(CONFIG_TOOLS)

        config.update(tools=tools)
        return config

    @cached_property
    def media(self):
        """
        Define the media files required by the widget.

        Returns:
            Media: Media assets required by the widget.
        """
        js_list = [
            '//cdn.jsdelivr.net/npm/@editorjs/editorjs@' + VERSION  # lib
        ]

        plugins = self.plugins or PLUGINS

        if plugins:
            js_list += ['//cdn.jsdelivr.net/npm/' + p for p in plugins]

        js_list.append('django-editorjs-fields/js/django-editorjs-fields.js')
        js_list.append('django-editorjs-fields/js/image_settings.js')

        return Media(
            js=js_list,
            css={
                'all': [

                ]
            },
        )

    def render(self, name, value, attrs=None, renderer=None):
        """
        Render the widget.

        Args:
            name (str): The name of the widget.
            value (str): The value of the widget.
            attrs (dict): Additional attributes for the widget.
            renderer: The renderer for the widget.

        Returns:
            str: Rendered HTML of the widget.
        """
        if value is None:
            value = ''

        if renderer is None:
            renderer = get_default_renderer()

        return mark_safe(renderer.render("django-editorjs-fields/widget.html", {
            'widget': {
                'name': name,
                'value': conditional_escape(force_str(value)),
                'attrs': self.build_attrs(self.attrs, attrs),
                'config': json_encode(self.configuration()),
            }
        }))
