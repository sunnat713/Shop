from django import template

register = template.Library()


@register.simple_tag
def get_lang_url(request, language):
    url = request.path.split('/')
    url[1] = language
    url = '/'.join(url)
    return url
    # url = request.path
    # url = '/' + language + url[3:]
    # return url


@register.simple_tag
def get_price_url(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return "null"

