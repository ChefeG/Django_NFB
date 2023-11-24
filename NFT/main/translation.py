from modeltranslation.translator import register, TranslationOptions
from .models import ModelNewsLine, ModelСover, ModelMatches, ModelTeams, ModelTopPlayer, ModelStatistics, \
    ModelTopMatches, ModelAnnouncements

@register(ModelMatches)
class MatchesTranslationOptions(TranslationOptions):
    fields = ('team_1', 'team_2', 'date', 'venue')
