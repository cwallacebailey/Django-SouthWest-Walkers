from django.test import TestCase
from .forms import PostForm

class TestPostForm(TestCase):

    def test_form_title(self):
        form = PostForm({'post_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('post_title', form.errors.keys())
        self.assertEqual(form.errors['post_title'][0], 'This field is required.')

    def test_form_title_present(self):
        form = PostForm({'post_title': 'Nice Walk'})
        self.assertTrue(form.is_valid())

    def test_fields_are_showing_correctly(self):
        form = PostForm
        self.assertEqual(form.Meta.fields, ['post_title', ])