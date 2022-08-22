from django.test import TestCase

class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/create_profile')
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'create_profile.html')
