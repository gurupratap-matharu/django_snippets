LANGUAGES = ['python', 'javascript', 'rust', 'c', 'haskell',
             'R', 'go', 'typescript', 'ruby', 'c#', 'bash', 'perl', 'php']
SNIPPETS = [
    """
    class ChoiceProvider(BaseProvider):
        def random_choice(self, choices=None):
            "Given a list of choices in Django format, return a random value"
            choice = self.random_element(choices)
            return choice[0]
    """,
    """
    from somefile import ChoiceProvider
    factory.Faker.add_provider(ChoiceProvider)
    """,
    """
    class FooTests(unittest.TestCase):
        def test_with_factory_boy(self):
            # We need a 200€, paid order, shipping to australia, for a VIP customer
            order = OrderFactory(
                amount=200,
                status='PAID',
                customer__is_vip=True,
                address__country='AU',
            )
            # Run the tests here

        def test_without_factory_boy(self):
            address = Address(
                street="42 fubar street",
                zipcode="42Z42",
                city="Sydney",
                country="AU",
            )
            customer = Customer(
                first_name="John",
                last_name="Doe",
                phone="+1234",
                email="john.doe@example.org",
                active=True,
                is_vip=True,
                address=address,
            )
    """,
    """
    $ git clone git://github.com/FactoryBoy/factory_boy/
    $ python setup.py install
    """,
    """
    import factory
    from . import models

    class UserFactory(factory.Factory):
        class Meta:
            model = models.User

        first_name = 'John'
        last_name = 'Doe'
        admin = False

    # Another, different, factory for the same object
    class AdminFactory(factory.Factory):
        class Meta:
            model = models.User

        first_name = 'Admin'
        last_name = 'User'
        admin = True

    """,
    """
    >>> users = UserFactory.build_batch(10, first_name="Joe")
    >>> len(users)
    10
    >>> [user.first_name for user in users]
    ["Joe", "Joe", "Joe", "Joe", "Joe", "Joe", "Joe", "Joe", "Joe", "Joe"]
    """,
]
