import factory
from snippets.models import Language, Snippet
from snippets.tests.config import LANGUAGES, SNIPPETS
from users.factories import UserFactory


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language
        django_get_or_create = ('name',)

    name = factory.Faker('random_element', elements=LANGUAGES)
    slug = factory.LazyAttribute(lambda obj: obj.name)


class SnippetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Snippet
    user = factory.SubFactory(UserFactory)
    language = factory.SubFactory(LanguageFactory)
    name = factory.Faker('catch_phrase')
    description = factory.Faker('paragraph')
    snippet = factory.Faker('random_element', elements=SNIPPETS)
    public = factory.Faker('boolean')
