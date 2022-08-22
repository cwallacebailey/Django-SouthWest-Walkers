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

    # def test_adding_new_post(self):
    #     """
    #     ensure a new post can be added
    #     check object list for Post model
    #     is 1 once post has been created
    #     """
    #     temp_user = User.objects.create(username = "user")
    #     instance = self.client.post('/add_post/', {'post_title': 'Nice Walk', 'post_author': temp_user, 'distance': 100, 'created_date': 'Aug. 14, 2022, 12:45 p.m', 'body': 'test'})
    #     # self.assertEqual(Post.objects.last().post_title, "Nice Walk")
    #     print(instance.post_title)
    #     # self.assertEqual(instance.status_code, 200)
        
        # self.assertEqual(len(post_objects), 1)

    # def test_deleting_post(self):
    #     """
    #     ensure a post can be deleted
    #     check object list for Post model
    #     is 0 once post has been created
    #     """
    #     temp_user = User.objects.create(username = "user")
    #     temp_post = Post.objects.create(post_title = 'Nice Walk', post_author = temp_user, distance = 100, created_date = 'Aug. 14, 2022, 12:45 p.m', body = 'test')
    #     response = self.client.get(f'delete/{temp_post.id}')
    #     post_objects = Post.objects.filter(id=temp_post.id)
    #     self.assertEqual(len(post_objects), 0)

    # def test_updating_post(self):
    #     temp_user = User.objects.create(username = "user")
    #     temp_post = Post.objects.create(post_title = 'Nice Walk', post_author = temp_user, distance = 100, created_date = 'Aug. 14, 2022, 12:45 p.m', body = 'test')
    #     response = self.client.get(f'delete/{temp_post.id}')

    def test_get_user_profile(self):

        self.client = Client()
        temp_user = User.objects.create(username = "user", password="te4321st?")

        self.client.login(
            username = "user", password="te4321st?"
        )

        profile = Profile.objects.create(display_name = "test1", user = temp_user)
        response = self.client.get('/profile/1') #https://stackoverflow.com/questions/47111777/how-do-i-test-a-django-createview/47112524#47112524
        # self.assertEqual(response.status_code, 200)

    # def get_success_url(self):
    #     pk = self.kwargs["pk"]
    #     return reverse("profile", kwargs={"pk": pk})

    # def test_get_post_detail(self):
    #     temp_user = User.objects.create(username = "user")
    #     temp_post = Post.objects.create(post_title = 'Nice Walk', post_author = temp_user, distance = 100, created_date = 'Aug. 14, 2022, 12:45 p.m', body = 'test')
    #     response = self.client.get(f'detail/{temp_post.id}')
    #     self.assertEqual(response.status_code, 200)
