""" Contains module for testing page app views """
from django.test import Client, TestCase

from ..models import Article

class ArticleViewsTestCase(TestCase):
	""" Case for testing article views """
	def setUp(self):
		""" setup test environment """
		Article.objects.create(id=1, title="my_test_title", html="<p>test_page_1</p>", tags="one,two,three", work_in_progress=False)
		Article.objects.create(id=2, title="my_test_new", html="<p>following page</p>", work_in_progress=False)
		Article.objects.create(id=3, title="my_test_wip", html="<p>page being written</p>", work_in_progress=True)

	def test_index_page_response(self):
		""" Check index page content and response """
		client = Client()
		resp = client.get('/page/')
		content = str(resp.content)
		self.assertEqual(resp.status_code, 200)
		self.assertIn('my_test_title', content)
		self.assertIn('my_test_new', content)
		# make sure the page with work in progress set as True does not appear on index page
		self.assertNotIn('my_test_wip', content)

	def test_show_page_by_id(self):
		""" Check content of the show_page view """
		client = Client()
		resp = client.get('/page/1/')
		content = str(resp.content)
		self.assertIn('my_test_title', content)
		self.assertIn('test_page_1', content)
		self.assertNotIn('my_test_new', content)
		self.assertNotIn('my_test_wip', content)
