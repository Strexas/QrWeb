"""Module containing functions for generating HTML elements from Editor.js data."""
import json

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def generate_paragraph(data):
    """Generate HTML paragraph element."""
    text = data.get('text').replace('&nbsp;', ' ')
    return f'<p>{text}</p>'


def generate_list(data):
    """Generate HTML list element."""
    list_li = ''.join([f'<li>{item}</li>' for item in data.get('items')])
    tag = 'ol' if data.get('style') == 'ordered' else 'ul'
    return f'<{tag}>{list_li}</{tag}>'


def generate_header(data):
    """Generate HTML header element."""
    text = data.get('text').replace('&nbsp;', ' ')
    level = data.get('level')
    return f'<h{level}>{text}</h{level}>'


def generate_image(data):
    """Generate HTML image element."""
    url = data.get('file', {}).get('url')
    caption = data.get('caption')
    classes = []

    if data.get('stretched'):
        classes.append('stretched')
    if data.get('withBorder'):
        classes.append('withBorder')
    if data.get('withBackground'):
        classes.append('withBackground')

    classes = ' '.join(classes)

    return f'<img src="{url}" alt="{caption}" class="{classes}" />'


def generate_delimiter():
    """Generate HTML delimiter element."""
    return '<div class="delimiter"></div>'


def generate_table(data):
    """Generate HTML table element."""
    rows = data.get('content', [])
    table = ''

    for row in rows:
        table += '<tr>'
        for cell in row:
            table += f'<td>{cell}</td>'
        table += '</tr>'

    return f'<table>{table}</table>'


def generate_warning(data):
    """Generate HTML warning element."""
    title, message = data.get('title'), data.get('message')

    if title:
        title = f'<div class="alert__title">{title}</div>'
    if message:
        message = f'<div class="alert__message">{message}</div>'

    return f'<div class="alert">{title}{message}</div>'


def generate_quote(data):
    """Generate HTML quote element."""
    alignment = data.get('alignment')
    caption = data.get('caption')
    text = data.get('text')

    if caption:
        caption = f'<cite>{caption}</cite>'

    classes = f'align-{alignment}' if alignment else None

    return f'<blockquote class="{classes}">{text}{caption}</blockquote>'


def generate_code(data):
    """Generate HTML code element."""
    code = data.get('code')
    return f'<code class="code">{code}</code>'


def generate_raw(data):
    """Generate HTML raw element."""
    return data.get('html')


def generate_embed(data):
    """Generate HTML embed element."""
    service = data.get('service')
    caption = data.get('caption')
    embed = data.get('embed')
    iframe = f'<iframe src="{embed}" allow="autoplay" allowfullscreen="allowfullscreen"></iframe>'

    return f'<div class="embed {service}">{iframe}{caption}</div>'


def generate_link(data):
    """Generate HTML link element."""

    link, meta = data.get('link'), data.get('meta')

    if not link or not meta:
        return ''

    title = meta.get('title')
    description = meta.get('description')
    image = meta.get('image')

    wrapper = (f'<div class="link-block"><a href="{ link }" '
               f'target="_blank" rel="nofollow noopener noreferrer">')

    if image.get('url'):
        image_url = image.get('url')
        wrapper += (f'<div class="link-block__image"'
                    f' style="background-image: url(\'{image_url}\');"></div>')

    if title:
        wrapper += f'<p class="link-block__title">{title}</p>'

    if description:
        wrapper += f'<p class="link-block__description">{description}</p>'

    wrapper += f'<p class="link-block__link">{link}</p>'
    wrapper += '</a></div>'
    return wrapper


@register.filter(is_safe=True)
def editorjs(value):
    """Convert Editor.js data to HTML."""
    if not value or value == 'null':
        return ""

    if not isinstance(value, dict):
        try:
            value = json.loads(value)
        except ValueError:
            return value
        except TypeError:
            return value

    html_list = []
    type_handlers = {
        'paragraph': generate_paragraph,
        'header': generate_header,
        'list': generate_list,
        'image': generate_image,
        'delimiter': generate_delimiter,
        'warning': generate_warning,
        'table': generate_table,
        'code': generate_code,
        'raw': generate_raw,
        'embed': generate_embed,
        'quote': generate_quote,
        'linktool': generate_link,
    }

    # Iterate over items in value['blocks']
    for item in value['blocks']:
        types, data = item.get('type'), item.get('data')
        types = types.lower()

        # Check if the type is in the dictionary
        if types in type_handlers:
            # Call the corresponding generator function
            html_list.append(type_handlers[types](data))

    # Join the html_list and return the result
    return mark_safe(''.join(html_list))
