
import discord

from discord import app_commands
from discord.app_commands.translator import locale_str, TranslationContextTypes
from fluent.runtime import FluentLocalization, FluentResourceLoader
from typing import Any



class CustomTranslator(app_commands.Translator):
    def __init__(self):
        # load any resources when the translator initialises.
        # if asynchronous setup is needed, override `Translator.load()`!
        self.resources = FluentResourceLoader('aneko/locale/{locale}')
        self.mapping = {
            discord.Locale.brazil_portuguese: FluentLocalization(['pt-BR'], ['commands.ftl'], self.resources),
            discord.Locale.american_english: FluentLocalization(['en-US'], ['commands.ftl'], self.resources)
            }
        self.mapping_response = {
            discord.Locale.brazil_portuguese: FluentLocalization(['pt-BR'], ['response.ftl'], self.resources),
            discord.Locale.american_english: FluentLocalization(['en-US'], ['response.ftl'], self.resources)
        }


    async def translate(self, string: locale_str, locale: discord.Locale, context: TranslationContextTypes):
        """core translate method called by the library"""

        fluent_id = string.extras.get('fluent_id')
        if not fluent_id:
            # ignore strings without an attached fluent_id
            return string.message

        l10n = self.mapping.get(locale)
        if not l10n:
            # no translation available for this locale
            return string.message

        # otherwise, a translation is assumed to exist and is returned
        if localised := l10n.format_value(fluent_id):
            if localised != fluent_id:
                return localised
    
        return string.message
    

    async def localise(self, string: locale_str, locale: discord.Locale, **params: Any):
        """translates a given string for a locale, subsituting any required parameters.
        meant to be called for things outside what discord handles, eg. a message sent from the bot
        """

        l10n = self.mapping_response.get(locale)
        if not l10n:
            # return the string untouched
            return string.message

        # strings passed to this method need to include a fluent_id extra
        # since we are trying to explicitly localise a string
        fluent_id = string.extras['fluent_id']

        if localised := l10n.format_value(fluent_id, params):
            if localised != fluent_id:
                return localised
        
        return string.message