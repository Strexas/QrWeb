"""Module containing functions for generating HTML elements from Editor.js data."""
import json

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def generate_paragraph(data):
    """Generate HTML paragraph element."""
    text = data.get('text').replace('&nbsp;', ' ')
    classes = ['ce-paragraph', 'cdx-block']  # Default classes

    align = data.get('alignment')
    # Add additional classes based on data
    if 'left' in align:
        classes.append('ce-paragraph--left')
    elif 'center' in align:
        classes.append('ce-paragraph--center')
    elif 'right' in align:
        classes.append('ce-paragraph--right')
    elif 'justify' in align:
        classes.append('ce-paragraph--justify')

    classes = ' '.join(classes)

    return f'<p class="{classes}">{text}</p>'


def generate_list(data):
    """Generate HTML list element."""
    list_li = ''.join([f'<li>{item}</li>' for item in data.get('items')])
    tag = 'ol class="cdx-block cdx-list cdx-list--ordered"' if data.get('style') == 'ordered' else \
        'ul class="cdx-block cdx-list cdx-list--unordered"'
    return f'<{tag}>{list_li}</{tag}>'


def generate_header(data):
    """Generate HTML header element."""
    text = data.get('text').replace('&nbsp;', ' ')
    level = data.get('level')
    align = data.get('alignment')
    classes = ['ce-header']  # Default classes

    # Add additional classes based on alignment data
    if 'left' in align:
        classes.append('ce-header--left')
    elif 'center' in align:
        classes.append('ce-header--center')
    elif 'right' in align:
        classes.append('ce-header--right')
    elif 'justify' in align:
        classes.append('ce-header--justify')

    classes = ' '.join(classes)

    return f'<h{level} class="{classes}">{text}</h{level}>'


def generate_image(data):
    """Generate HTML image element."""
    url = data.get('file', {}).get('url')
    caption = data.get('caption')
    classes = ['image-tool__image-picture']

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
        table += '<tr class="tc-row">'
        for cell in row:
            table += f'<td class="tc-cell">{cell}</td>'
        table += '</tr>'

    return f'<table class="tc-table">{table}</table>'


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
    iframe = (f'<iframe src="{embed}" allow="autoplay" allowfullscreen="allowfullscreen" style="width: 100%; height: '
              f'400px;"></iframe>')
    div_style = 'style="display: flex; justify-content: center;"'

    return f'<div class="embed {service}" {div_style}>{iframe}{caption}</div>'


def generate_link(data):
    """Generate HTML link element."""
    link, meta = data.get('link'), data.get('meta')

    if not link or not meta:
        return ''

    # Limit for link display
    max_link_length = 30
    display_link = link[:max_link_length] + ('...' if len(link) > max_link_length else '')

    title = meta.get('title')
    description = meta.get('description')
    image = meta.get('image')

    wrapper = (f'<div class="link-tool">'
               f'<a class="link-tool__content link-tool__content--rendered--view" href="{link}" '
               f'target="_blank" rel="nofollow noopener noreferrer">')

    if image and image.get('url'):
        image_url = image.get('url')
        wrapper += (f'<div class="link-tool__image" '
                    f'style="background-image: url(\'{image_url}\');"></div>')

    wrapper += '<div class="link-tool__info">'

    if title:
        wrapper += f'<p class="link-tool__title">{title}</p>'

    if description:
        wrapper += f'<p class="link-tool__description">{description}</p>'

    wrapper += f'<p class="link-tool__anchor">{display_link}</p>'
    wrapper += '</div>'
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
