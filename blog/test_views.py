from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import Profile, Post
from django.contrib.auth.models import User
from django.test.utils import override_settings

class TestViews(TestCase):

    @override_settings(DEBUG=True)
    def test_get_home_page(self):
        """
        ensure page can be reached and
        template used is correct
        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_home_page_by_name(self):
        """
        ensure page can be reached and
        using its reverse title
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_get_about_page_by_name(self):
        """
        ensure page can be reached and
        using its reverse title
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_get_create_profile(self):
        """
        ensure page can be reached and
        template used is correct
        """
        response = self.client.get('/create_profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_profile.html')

    def test_get_create_profile_by_name(self):
        """
        ensure page can be reached and
        using its reverse title
        """
        response = self.client.get(reverse('create_profile'))
        self.assertEqual(response.status_code, 200)
    
    def test_get_add_post(self):
        """
        ensure page can be reached and
        template used is correct
        """
        response = self.client.get('/add_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_post.html')

    def test_get_add_post_by_name(self):
        """
        ensure page can be reached and
        using its reverse title
        """
        response = self.client.get(reverse('add_post'))
        self.assertEqual(response.status_code, 200)