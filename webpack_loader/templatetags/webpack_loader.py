from django import template, VERSION
from django.utils.safestring import mark_safe

from .. import utils

register = template.Library()


BUNDLE_TAGS_META_KEY = 'BUNDLE_TAGS'


@register.simple_tag(takes_context=True)
def render_bundle(context, bundle_name, extension=None, config='DEFAULT', attrs='', request=None):
    req = context.request
    tags = set(utils.get_as_tags(bundle_name, extension=extension, config=config, attrs=attrs))
    rendered_tags = req.META.get(BUNDLE_TAGS_META_KEY)
    if rendered_tags is not None:
        req.META[BUNDLE_TAGS_META_KEY] = rendered_tags.union(tags)
    else:
        rendered_tags = set()
        req.META[BUNDLE_TAGS_META_KEY] = tags
    tags_not_yet_rendered = tags.difference(rendered_tags)
    # tags_already_rendered = tags.intersection(rendered_tags)
    # print('Rendering tags for {}'.format(bundle_name))
    # print('Already have tags: {}'.format(len(tags_already_rendered)))
    # print('Rendering tags: {}'.format(len(tags_not_yet_rendered)))
    return mark_safe('\n'.join(tags_not_yet_rendered))


@register.simple_tag
def webpack_static(asset_name, config='DEFAULT'):
    return utils.get_static(asset_name, config=config)


assignment_tag = register.simple_tag if VERSION >= (1, 9) else register.assignment_tag
@assignment_tag
def get_files(bundle_name, extension=None, config='DEFAULT'):
    """
    Returns all chunks in the given bundle.
    Example usage::

        {% get_files 'editor' 'css' as editor_css_chunks %}
        CKEDITOR.config.contentsCss = '{{ editor_css_chunks.0.publicPath }}';

    :param bundle_name: The name of the bundle
    :param extension: (optional) filter by extension
    :param config: (optional) the name of the configuration
    :return: a list of matching chunks
    """
    return utils.get_files(bundle_name, extension=extension, config=config)
