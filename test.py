
import unittest 
from main import app

class ExampleTest(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client() 

	def tearDown(self):
		pass 

	def test_homepage(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code,200)

	def test_detail(self):	
		response = self.app.get("/about")
		self.assertEqual(response.status_code,200)



if __name__ == '__main__':
	unittest.main()
