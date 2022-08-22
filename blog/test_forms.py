from django.test import TestCase
from .forms import PostForm, ProfileForm

class TestPostForm(TestCase):

    def test_form_title(self):
        form = PostForm({'post_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('post_title', form.errors.keys())
        self.assertEqual(form.errors['post_title'][0], 'This field is required.')

    # def test_form_submission(self):
    #     form = PostForm({'post_title': 'Nice Walk', 'post_author': 'default', 'distance': 100, 'created_date': 'Aug. 14, 2022, 12:45 p.m'})
    #     self.assertTrue(form.is_valid())

    # def test_fields_are_showing_correctly(self):
    #     form = PostForm
    #     self.assertEqual(form.Meta.fields, ['post_title', 'header_image', 'distance', 'meters_climbed', 'first_cairn', 'body',])


class TestProfileForm(TestCase):

    def test_profile_form_empty_display_name(self):
        form = ProfileForm({'display_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('display_name', form.errors.keys())
        self.assertEqual(form.errors['display_name'][0], 'This field is required.')
    
    def test_profile_form_completed_display_name(self):
        form = ProfileForm({'display_name': 'Big_Chungus'})
        self.assertTrue(form.is_valid())

    def test_profile_form_completed_correct_social_links(self):
        form = ProfileForm({'display_name': 'Big_Chungus', 'instagram_url': 'https://www.instagram.com/', 'strava_url': 'https://www.strava.com', 'linkedin_url': 'https://www.linkedin.com'})
        self.assertTrue(form.is_valid())

    def test_profile_form_incorrect_instagram_links(self):
        form = ProfileForm({'display_name': 'Big_Chungus', 'instagram_url': 'www.facebook.com',})
        self.assertTrue(form.is_valid())

        
        