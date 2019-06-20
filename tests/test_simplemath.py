import simplemath as sm
import unittest

class TestSimpleMath(unittest.TestCase):

	def test_add_int(self):
		ret = sm.add(1, 3)
		self.assertEqual(ret, 4)

	def test_add_neg_int(self):
		ret = sm.add(-1, -3)
		self.assertEqual(ret, -4)

	def test_add_str(self):
		ret = sm.add("a", "b")
		self.assertEqual(ret, "ab")

	def test_main(self):
		ret = sm.main()
		self.assertEqual(ret, 4)

if __name__ == "__main__":
	unittest.main()