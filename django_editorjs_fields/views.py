"""Views for handling image upload, URL linking, and related operations."""

import json
import logging
import os
from io import BytesIO
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from PIL import Image

from .config import IMAGE_NAME, IMAGE_NAME_ORIGINAL, IMAGE_UPLOAD_PATH
from .utils import storage

LOGGER = logging.getLogger('django_editorjs_fields')


class ImageUploadView(View):
    """View for handling image upload."""

    http_method_names = ["post"]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Dispatch method for handling CSRF exemption."""
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        """Handle the POST request for image upload."""
        if 'image' in request.FILES:
            the_file = request.FILES['image']
            allowed_types = [
                'image/jpeg',
                'image/jpg',
                'image/pjpeg',
                'image/x-png',
                'image/png',
                'image/webp',
                'image/gif',
            ]
            if the_file.content_type not in allowed_types:
                return JsonResponse(
                    {'success': 0, 'message': 'You can only upload images.'}
                )

            image = Image.open(the_file)
            image_file = BytesIO()
            if image.width > 300 or image.height > 300:
                ratio = min(300 / image.width, 300 / image.height)
                new_width = int(image.width * ratio)
                new_height = int(image.height * ratio)
                image = image.resize((new_width, new_height))
                image.save(image_file, format='PNG')

            image_file.seek(0)
            filename, extension = os.path.splitext(the_file.name)

            if IMAGE_NAME_ORIGINAL is False:
                filename = IMAGE_NAME(filename=filename, file=the_file)

            filename += extension

            upload_path = os.path.join(IMAGE_UPLOAD_PATH, request.user.username)

            path = storage.save(
                os.path.join(upload_path, filename), image_file
            )
            link = storage.url(path)

            return JsonResponse({'success': 1, 'file': {"url": link}})
        return JsonResponse({'success': 0})


class LinkToolView(View):
    """View for handling URL linking."""

    http_method_names = ["get"]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Dispatch method for handling CSRF exemption."""
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        """Handle the GET request for URL linking."""
        url = request.GET.get('url', '')

        LOGGER.debug('Starting to get meta for: %s', url)

        validate = URLValidator(schemes=['https', 'https'])
        try:
            validate(url)
        except ValidationError as e:
            LOGGER.error(e)
            return JsonResponse({'success': 0})

        try:
            LOGGER.debug('Let\'s try to get meta from: %s', url)

            full_url = 'https://api.microlink.io/?' + urlencode({'url': url})

            req = Request(full_url, headers={
                'User-Agent': request.META.get('HTTP_USER_AGENT',
                                               'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
            })
            with urlopen(req) as res:
                res_body = res.read()
                res_json = json.loads(res_body.decode("utf-8"))

                if 'success' in res_json.get('status'):
                    data = res_json.get('data')

                    if data:
                        LOGGER.debug('Response meta: %s', data)
                        meta = {
                            'title': data.get('title'),
                            'description': data.get('description'),
                            'image': data.get('image')
                        }

                        return JsonResponse({
                            'success': 1,
                            'link': data.get('url', url),
                            'meta': meta
                        })

        except HTTPError as e:
            LOGGER.error('The server couldn\'t fulfill the request.')
            LOGGER.error('Error code: %s %s', e.code, e.msg)
        except URLError as e:
            LOGGER.error('We failed to reach a server. url: %s', url)
            LOGGER.error('Reason: %s', e.reason)

        return JsonResponse({'success': 0})


class ImageByUrl(View):
    """View for handling image upload from URL."""

    http_method_names = ["post"]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Dispatch method for handling CSRF exemption."""
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        """Handle the POST request for image upload from URL."""
        body = json.loads(request.body.decode())
        if 'url' in body:
            return JsonResponse({'success': 1, 'file': {"url": body['url']}})
        return JsonResponse({'success': 0})
