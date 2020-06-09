import unittest
import cap

class TextCap(unittest.TestCase):

	def test_one(self):
		text = "python"
		result = cap.cap_text(text)
		self.assertEqual(result,"Python")
		
	def test_multi(self):
		text = "monty python"
		result = cap.cap_text(text)
		self.assertEqual(result,"Monty Python")

if __name__=="__main__":
	unittest.main()
