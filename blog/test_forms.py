from django.test import TestCase
from .forms import PostForm, ProfileForm, CommentForm
from django.contrib.auth.models import User

class TestPostForm(TestCase):
    """
    Test for the Post form
    """

    def test_form_title(self):
        form = PostForm({'post_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('post_title', form.errors.keys())
        self.assertEqual(form.errors['post_title'][0], 'This field is required.')

    def test_form_submission(self):
        """
        Test that the display name must be entered
        for the form to be valid
        """
        user = User.objects.create(username = "user")
        form = PostForm({'post_title': 'Nice Walk 2', 'post_author': user, 'distance': 100, 'created_date': 'Aug. 14, 2022, 12:45 p.m', 'body': 'test', 'meters_climbed': 40})
        self.assertTrue(form.is_valid())


class TestProfileForm(TestCase):
    """
    Test for the Profile form
    """

    def test_profile_form_empty_display_name(self):
        """
        Test that the display name must be entered
        for the form to be valid
        """
        form = ProfileForm({'display_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('display_name', form.errors.keys())
        self.assertEqual(form.errors['display_name'][0], 'This field is required.')
    
    def test_profile_form_completed_display_name(self):
        """
        Test that only the display name needs to be entered
        for the form to be valid
        """
        form = ProfileForm({'display_name': 'Big_Chungus'})
        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):
    """
    Test for the comment form
    """
    
    def test_comment_form_empty(self):
        """
        Test that the body must be entered
        for the form to be valid
        """
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_comment_form_empty(self):
        """
        Test that the body must be entered
        for the form to be valid
        """
        form = CommentForm({'body': 'Test'})
        self.assertTrue(form.is_valid())

