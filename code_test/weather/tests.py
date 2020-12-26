from django.test import TestCase

# Create your tests here.
class WeatherTest(TestCase):
	
	def test_home_page_renders_home_template(self):
		
		response = self.client.get('')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')