from modeltranslation.translator import translator, TranslationOptions
from .models import Products

class NewsTranslationOptions(TranslationOptions):
    fields = ('product_name', )

translator.register(Products, NewsTranslationOptions)