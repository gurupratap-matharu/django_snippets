from django.test import TestCase
from django.urls import resolve, reverse
from snippets.tests.factories import SnippetFactory
from snippets.views import HomePageView
from users.factories import UserFactory


class HomePageTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.snippets = [SnippetFactory(user=self.user) for i in range(50)]

    def test_home_page_resolves_homepageview(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def test_home_page_works_for_anonymous_user(self):
        response = self.client.get(reverse('home'))
        no_response = self.client.get('homepage')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Django Snippets')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)

    def test_home_page_works_for_logged_in_user(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('home'))
        no_response = self.client.get('homepage')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Django Snippets')
        self.assertNotContains(response, 'Hi I should not be on this page')
        self.assertEqual(no_response.status_code, 404)

    def test_home_page_contains_only_public_snippets(self):
        response = self.client.get(reverse('home'))
        snippets_on_page = response.context_data['snippet_list']
        snippet_type = [s.public for s in snippets_on_page]
        print(snippet_type)
        self.assertTrue(snippet_type)

    def test_home_page_contains_paginated_snippets(self):
        response = self.client.get(reverse('home'))
        no_response = self.client.get('homepage')

        len_of_snippets_on_page = len(response.context_data['snippet_list'])
        self.assertEqual(len_of_snippets_on_page, 12)
