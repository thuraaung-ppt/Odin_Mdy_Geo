
import unittest 
from main import app


class Blueprint_Test(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()

	def test_homepage(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code,200)

	def test_about(self):	
		response = self.app.get("/about")
		self.assertEqual(response.status_code,200)

	def test_contact(self):
		response = self.app.get("/contact")
		self.assertEqual(response.status_code,200)

	def test_bns_leader(self):
		response = self.app.get("/bns")
		self.assertEqual(response.status_code,301)

	def test_cdt_parties(self):
		response = self.app.get("/cdt")
		self.assertEqual(response.status_code,301)

	def test_cele(self):		
		response = self.app.get("/cele")
		self.assertEqual(response.status_code,301)

	def test_mb_pmt(self):
		response = self.app.get("/mb")
		self.assertEqual(response.status_code,301)

	def test_modern_figures(self):
		response = self.app.get("/modern_figures")
		self.assertEqual(response.status_code,301)


if __name__ == '__main__':
	unittest.main()
