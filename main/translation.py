from modeltranslation.translator import register, TranslationOptions
from .models import Portfolio, ClientFeedback, Team, Service

@register(Portfolio)
class PortfolioTranslation(TranslationOptions):
    fields = ('title','description')


@register(ClientFeedback)
class ClientFeedbackTranslation(TranslationOptions):
    fields = ('comment',)

@register(Team)
class TeamTranslation(TranslationOptions):
    fields = ('bio','position')


@register(Service)
class ServiceTranslation(TranslationOptions):
    fields = ('title','description')