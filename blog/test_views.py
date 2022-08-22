from django.test import TestCase
from django.shortcuts import reverse
from .models import Profile, Post
from django.contrib.auth.models import User
from django.test.utils import override_settings

class TestViews(TestCase):

    @override_settings(DEBUG=True)
    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_home_page_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_get_about_page_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_get_create_profile(self):
        response = self.client.get('/create_profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_profile.html')

    def test_get_create_profile_by_name(self):
        response = self.client.get(reverse('create_profile'))
        self.assertEqual(response.status_code, 200)
    
    def test_get_add_post(self):
        response = self.client.get('/add_post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_post.html')

    # def test_get_user_profile(self):
    #     temp_user = User.objects.create(username = "user")
    #     profile = Profile.objects.create(display_name = "test1", user = temp_user)
    #     response = self.client.get(f'profile/{profile.pk}')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_update_profile(self):
    #     response = self.client.get('/create_profile')
    #     self.assertEqual(response.status_code, 200)

    # def test_get_post_detail(self):
    #     temp_user = User.objects.create(username = "user")
    #     temp_post = Post.objects.create(post_title = 'Nice Walk', post_author = temp_user, distance = 100, created_date = 'Aug. 14, 2022, 12:45 p.m', body = 'test')
    #     response = self.client.get(f'detail/{temp_post.id}')
    #     self.assertEqual(response.status_code, 200)
