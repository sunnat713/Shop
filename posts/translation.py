from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(PostModel)
class PostTranslationOption(TranslationOptions):
    fields = ('title', 'content')